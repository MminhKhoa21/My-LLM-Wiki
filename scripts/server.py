#!/usr/bin/env python3
import os
import re
import json
import sys
import urllib.parse
import http.server
import socketserver
import subprocess
from pathlib import Path
from datetime import datetime

# Paths
ROOT_DIR = Path(__file__).parent.parent
DASHBOARD_DIR = ROOT_DIR / "dashboard"
WIKI_DIR = ROOT_DIR / "wiki"
RAW_DIR = ROOT_DIR / "raw"
DRAFTS_DIR = ROOT_DIR / "drafts"

# Regex for frontmatter and links
YAML_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(\.?/?([^)]+\.md)\)")

def parse_frontmatter(content):
    match = YAML_RE.match(content)
    if not match:
        return None
    yaml_text = match.group(1)
    metadata = {}
    for line in yaml_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            if val.startswith('[') and val.endswith(']'):
                items = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                val = items
            metadata[key] = val
    return metadata

class WikiHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for local development ease
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, File-Name")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        if path.startswith("/api/"):
            self.handle_api_get(path, query)
        else:
            # Static file serving
            if path == "/" or path == "":
                file_path = DASHBOARD_DIR / "index.html"
            else:
                file_path = DASHBOARD_DIR / path.lstrip("/")

            # Security check
            try:
                resolved_file = file_path.resolve()
                resolved_dashboard = DASHBOARD_DIR.resolve()
                if not resolved_file.is_relative_to(resolved_dashboard):
                    self.send_error(403, "Forbidden")
                    return
            except Exception:
                self.send_error(404, "File Not Found")
                return

            if file_path.exists() and file_path.is_file():
                content_type = "text/html"
                if file_path.suffix == ".css":
                    content_type = "text/css"
                elif file_path.suffix == ".js":
                    content_type = "application/javascript"
                elif file_path.suffix == ".json":
                    content_type = "application/json"

                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(file_path.stat().st_size))
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File Not Found")

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == "/api/upload":
            self.handle_upload()
        elif path == "/api/run-indexer":
            self.handle_run_indexer()
        elif path == "/api/delete":
            self.handle_delete()
        elif path == "/api/clip":
            self.handle_clip()
        elif path == "/api/git-commit":
            self.handle_git_commit()
        elif path == "/api/cleanup-raw":
            self.handle_cleanup_raw()
        elif path == "/api/approve-draft":
            self.handle_approve_draft()
        elif path == "/api/reject-draft":
            self.handle_reject_draft()
        else:
            self.send_error(404, "API Endpoint Not Found")

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        response_bytes = json.dumps(data).encode("utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def handle_api_get(self, path, query):
        if path == "/api/notes":
            self.api_get_notes()
        elif path == "/api/note":
            self.api_get_note_detail(query)
        elif path == "/api/graph":
            self.api_get_graph()
        elif path == "/api/lint":
            self.api_get_lint()
        elif path == "/api/search":
            self.api_get_search(query)
        elif path == "/api/raw-files":
            self.api_get_raw_files()
        elif path == "/api/git-status":
            self.api_get_git_status()
        elif path == "/api/drafts":
            self.api_get_drafts()
        elif path == "/api/draft-detail":
            self.api_get_draft_detail(query)
        elif path == "/api/recent":
            self.api_get_recent()
        else:
            self.send_json({"error": "Endpoint not found"}, 404)

    def api_get_notes(self):
        notes = []
        if not WIKI_DIR.exists():
            self.send_json([])
            return
        
        for file_path in WIKI_DIR.glob("*.md"):
            if file_path.name in ["index.md", "log.md"]:
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                meta = parse_frontmatter(content) or {}
                notes.append({
                    "name": file_path.stem,
                    "title": meta.get("title", file_path.stem),
                    "description": meta.get("description", ""),
                    "type": meta.get("type", "unknown"),
                    "tags": meta.get("tags", []),
                    "timestamp": meta.get("timestamp", "")
                })
            except Exception as e:
                pass
        self.send_json(notes)

    def api_get_note_detail(self, query):
        note_name = query.get("name", [None])[0]
        if not note_name:
            self.send_json({"error": "Missing parameter 'name'"}, 400)
            return

        file_path = WIKI_DIR / f"{note_name}.md"
        if not file_path.exists() or not file_path.is_file():
            self.send_json({"error": f"Note '{note_name}' not found"}, 404)
            return

        try:
            content = file_path.read_text(encoding="utf-8")
            meta = parse_frontmatter(content) or {}
            # Strip YAML block from HTML display
            body_content = content
            match = YAML_RE.match(content)
            if match:
                body_content = content[match.end():].strip()

            self.send_json({
                "name": note_name,
                "meta": meta,
                "markdown": body_content
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_graph(self):
        nodes = []
        edges = []
        all_stems = set()

        if not WIKI_DIR.exists():
            self.send_json({"nodes": [], "edges": []})
            return

        # Phase 1: Collect nodes
        for file_path in WIKI_DIR.glob("*.md"):
            stem = file_path.stem
            all_stems.add(stem)
            
            # Treat index, log, overview as standard group types
            group_type = "system"
            if stem not in ["index", "log"]:
                try:
                    content = file_path.read_text(encoding="utf-8")
                    meta = parse_frontmatter(content) or {}
                    group_type = meta.get("type", "concept")
                except Exception:
                    group_type = "concept"
            else:
                group_type = "system"

            nodes.append({
                "id": stem,
                "label": stem.replace("_", " ").title() if stem not in ["index", "log"] else stem.upper(),
                "group": group_type
            })

        # Phase 2: Collect edges
        for file_path in WIKI_DIR.glob("*.md"):
            source_stem = file_path.stem
            try:
                content = file_path.read_text(encoding="utf-8")
                # Remove code blocks
                clean_content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
                clean_content = re.sub(r"`.*?`", "", clean_content)
                
                # Find links
                wikilinks = WIKILINK_RE.findall(clean_content)
                md_links = MARKDOWN_LINK_RE.findall(clean_content)
                
                targets = set(wikilinks)
                for link in md_links:
                    targets.add(Path(link).stem)

                for t in targets:
                    t_clean = t.strip()
                    t_alt = t_clean.replace(" ", "_")
                    
                    if t_clean in all_stems:
                        edges.append({"from": source_stem, "to": t_clean})
                    elif t_alt in all_stems:
                        edges.append({"from": source_stem, "to": t_alt})
            except Exception:
                pass

        self.send_json({"nodes": nodes, "edges": edges})

    def api_get_lint(self):
        script_path = ROOT_DIR / "scripts" / "linter.py"
        try:
            res = subprocess.run(["python", str(script_path)], capture_output=True, text=True, encoding="utf-8")
            self.send_json({
                "status": "success" if res.returncode == 0 else "lint_issues",
                "report": res.stdout
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_search(self, query):
        q = query.get("q", [None])[0]
        if not q:
            self.send_json({"error": "Missing parameter 'q'"}, 400)
            return

        script_path = ROOT_DIR / "scripts" / "search.py"
        try:
            res = subprocess.run(["python", str(script_path), "--query", q], capture_output=True, text=True, encoding="utf-8")
            self.send_json({
                "results": res.stdout
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_upload(self):
        content_length = int(self.headers.get('Content-Length', 0))
        file_name = self.headers.get('File-Name', 'uploaded_source.txt')
        
        # Sanitize filename
        file_name = Path(file_name).name
        if not file_name:
            self.send_json({"error": "Invalid file name"}, 400)
            return

        try:
            file_data = self.rfile.read(content_length)
            dest_path = RAW_DIR / file_name
            RAW_DIR.mkdir(parents=True, exist_ok=True)
            
            dest_path.write_bytes(file_data)
            
            # Trigger auto-ingestion pipeline in background
            auto_ingest_path = ROOT_DIR / "scripts" / "auto_ingest.py"
            subprocess.Popen(["python", str(auto_ingest_path), "--file", str(dest_path)])
            
            self.send_json({
                "status": "success",
                "message": f"Uploaded raw/{file_name}. AI auto-ingestion pipeline triggered."
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_run_indexer(self):
        script_path = ROOT_DIR / "scripts" / "indexer.py"
        try:
            res = subprocess.run(["python", str(script_path)], capture_output=True, text=True, encoding="utf-8")
            self.send_json({
                "status": "success",
                "message": res.stdout
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_raw_files(self):
        raw_files = []
        if not RAW_DIR.exists():
            self.send_json([])
            return
        try:
            for file_path in RAW_DIR.glob("*"):
                if file_path.is_file():
                    raw_files.append({
                        "name": file_path.name,
                        "size": file_path.stat().st_size
                    })
            self.send_json(raw_files)
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_delete(self):
        content_length = int(self.headers.get('Content-Length', 0))
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)
            ftype = params.get("type")
            name = params.get("name")
            
            if not ftype or not name:
                self.send_json({"error": "Missing parameters 'type' or 'name'"}, 400)
                return
                
            if ftype == "wiki":
                if name in ["index", "log", "overview"]:
                    self.send_json({"error": "Deletion of system core files is blocked"}, 400)
                    return
                file_path = WIKI_DIR / f"{name}.md"
            elif ftype == "raw":
                file_path = RAW_DIR / name
            else:
                self.send_json({"error": "Invalid file type"}, 400)
                return
                
            if not file_path.exists() or not file_path.is_file():
                self.send_json({"error": f"File '{name}' not found"}, 404)
                return
                
            # Perform deletion
            file_path.unlink()
            
            # Run indexer
            indexer_path = ROOT_DIR / "scripts" / "indexer.py"
            subprocess.run(["python", str(indexer_path)], capture_output=True)
            
            # Log the deletion to log.md
            log_path = WIKI_DIR / "log.md"
            if log_path.exists():
                try:
                    log_content = log_path.read_text(encoding="utf-8")
                    from datetime import datetime
                    curr_date = datetime.now().strftime("%Y-%m-%d")
                    log_entry = f"\n\n## [{curr_date}] system | Deletion of {ftype} file\n- Deleted file: {file_path.name}\n- Automatically ran indexer script."
                    log_path.write_text(log_content + log_entry, encoding="utf-8")
                except Exception:
                    pass
            
            self.send_json({
                "status": "success",
                "message": f"Successfully deleted {ftype} file: {file_path.name}"
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_clip(self):
        content_length = int(self.headers.get('Content-Length', 0))
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)
            url = params.get("url")
            name = params.get("name", "")
            
            if not url:
                self.send_json({"error": "Missing parameter 'url'"}, 400)
                return
                
            script_path = ROOT_DIR / "scripts" / "clip_webpage.py"
            cmd = ["python", str(script_path), "--url", url]
            if name:
                cmd += ["--name", name]
                
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            
            if res.returncode == 0:
                # Run auto-ingest in background for each saved file
                stdout_text = res.stdout
                raw_files = re.findall(r'raw/([a-zA-Z0-9_\-\.]+)', stdout_text)
                
                auto_ingest_path = ROOT_DIR / "scripts" / "auto_ingest.py"
                for rf in set(raw_files):
                    rf_path = RAW_DIR / rf
                    if rf_path.exists():
                        subprocess.Popen(["python", str(auto_ingest_path), "--file", str(rf_path)])
                        
                self.send_json({
                    "status": "success",
                    "message": res.stdout.strip() + " (AI auto-ingestion triggered)"
                })
            else:
                self.send_json({"error": res.stderr.strip() or res.stdout.strip()}, 500)
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_git_status(self):
        try:
            res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, encoding="utf-8")
            status_output = res.stdout.strip()
            is_clean = len(status_output) == 0
            self.send_json({
                "status": "success",
                "is_clean": is_clean,
                "output": status_output
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_git_commit(self):
        content_length = int(self.headers.get('Content-Length', 0))
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)
            message = params.get("message", "").strip()
            
            if not message:
                self.send_json({"error": "Commit message is required"}, 400)
                return
                
            # Stage all changes
            subprocess.run(["git", "add", "."], capture_output=True)
            
            # Commit
            res = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True, encoding="utf-8")
            
            if res.returncode == 0:
                self.send_json({
                    "status": "success",
                    "message": f"Committed successfully:\n{res.stdout.strip()}"
                })
            else:
                self.send_json({"error": f"Failed to commit:\n{res.stderr.strip() or res.stdout.strip()}"}, 500)
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_cleanup_raw(self):
        try:
            referenced_files = set()
            
            # 1. Parse all wiki markdown files frontmatter to get referenced raw sources
            for p in WIKI_DIR.glob("*.md"):
                if p.name not in ["index.md", "log.md", "overview.md"]:
                    try:
                        content = p.read_text(encoding="utf-8")
                        match = re.search(r"sources:\s*\[(.*?)\]", content)
                        if match:
                            sources_list = match.group(1).split(",")
                            for s in sources_list:
                                s = s.strip().strip('"').strip("'")
                                if s.startswith("raw/"):
                                    referenced_files.add(Path(s).name)
                    except Exception:
                        pass
                        
            # 2. Scan raw/ directory for files
            deleted_files = []
            space_freed = 0
            
            if RAW_DIR.exists():
                for p in RAW_DIR.glob("*"):
                    if p.is_file():
                        # If not referenced, delete it
                        if p.name not in referenced_files:
                            file_size = p.stat().st_size
                            p.unlink()
                            deleted_files.append(p.name)
                            space_freed += file_size
                            
            self.send_json({
                "status": "success",
                "deleted_count": len(deleted_files),
                "deleted_files": deleted_files,
                "space_freed_bytes": space_freed
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_drafts(self):
        try:
            drafts = []
            if DRAFTS_DIR.exists():
                for p in DRAFTS_DIR.glob("*.md"):
                    if p.is_file() and p.name != ".gitkeep":
                        content = p.read_text(encoding="utf-8")
                        # Extract helper comments
                        target_match = re.search(r"<!--\s*target:\s*(.*?)\s*-->", content)
                        title_match = re.search(r"<!--\s*title:\s*(.*?)\s*-->", content)
                        
                        target = target_match.group(1) if target_match else f"wiki/{p.name}"
                        title = title_match.group(1) if title_match else p.name.replace(".md", "").replace("_", " ").capitalize()
                        
                        # Find tags if any from frontmatter
                        tags = []
                        tags_match = re.search(r"tags:\s*\[(.*?)\]", content)
                        if tags_match:
                            tags = [t.strip().strip('"').strip("'") for t in tags_match.group(1).split(",") if t.strip()]
                            
                        # Find type
                        type_val = "concept"
                        type_match = re.search(r"type:\s*(\w+)", content)
                        if type_match:
                            type_val = type_match.group(1).strip()
                            
                        drafts.append({
                            "name": p.name,
                            "title": title,
                            "target": target,
                            "type": type_val,
                            "tags": tags,
                            "timestamp": datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                        })
            # Sort by newest draft modification time
            drafts.sort(key=lambda x: x["timestamp"], reverse=True)
            self.send_json(drafts)
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_draft_detail(self, query):
        name = query.get("name", [None])[0]
        if not name:
            self.send_json({"error": "Missing parameter 'name'"}, 400)
            return
            
        draft_path = DRAFTS_DIR / name
        if not draft_path.exists() or not draft_path.is_file():
            self.send_json({"error": f"Draft '{name}' not found"}, 404)
            return
            
        try:
            content = draft_path.read_text(encoding="utf-8")
            self.send_json({
                "name": name,
                "content": content
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def api_get_recent(self):
        try:
            recent = []
            for p in WIKI_DIR.glob("*.md"):
                if p.name not in ["index.md", "log.md", "overview.md"]:
                    try:
                        content = p.read_text(encoding="utf-8")
                        title = p.name.replace(".md", "").replace("_", " ").capitalize()
                        type_val = "concept"
                        timestamp = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
                        
                        # Extract yaml info
                        fm_match = YAML_RE.search(content)
                        if fm_match:
                            fm_text = fm_match.group(1)
                            t_match = re.search(r"title:\s*\"(.*?)\"", fm_text)
                            if t_match: title = t_match.group(1)
                            
                            ty_match = re.search(r"type:\s*(\w+)", fm_text)
                            if ty_match: type_val = ty_match.group(1).strip()
                            
                            ts_match = re.search(r"timestamp:\s*([\d\-]+)", fm_text)
                            if ts_match: timestamp = ts_match.group(1).strip()
                            
                        recent.append({
                            "name": p.name.replace(".md", ""),
                            "title": title,
                            "type": type_val,
                            "timestamp": timestamp
                        })
                    except Exception:
                        pass
            # Sort by timestamp descending
            recent.sort(key=lambda x: x["timestamp"], reverse=True)
            self.send_json(recent[:5])
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_approve_draft(self):
        content_length = int(self.headers.get('Content-Length', 0))
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)
            name = params.get("name")
            new_content = params.get("content", "").strip()
            
            if not name or not new_content:
                self.send_json({"error": "Parameters 'name' and 'content' are required"}, 400)
                return
                
            draft_path = DRAFTS_DIR / name
            if not draft_path.exists():
                self.send_json({"error": f"Draft '{name}' not found"}, 404)
                return
                
            # Extract target destination
            target_match = re.search(r"<!--\s*target:\s*(.*?)\s*-->", new_content)
            title_match = re.search(r"<!--\s*title:\s*(.*?)\s*-->", new_content)
            
            target = target_match.group(1) if target_match else f"wiki/{name}"
            title = title_match.group(1) if title_match else name.replace(".md", "").replace("_", " ").capitalize()
            
            # Clean up target content (strip the helper comments)
            clean_content = re.sub(r"<!--\s*target:\s*.*?\s*-->\n?", "", new_content)
            clean_content = re.sub(r"<!--\s*title:\s*.*?\s*-->\n?", "", clean_content).strip()
            
            # Make sure it writes to correct location
            dest_file = ROOT_DIR / target
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to wiki/
            dest_file.write_text(clean_content, encoding="utf-8")
            
            # Remove from drafts/
            draft_path.unlink()
            
            # Run indexer
            indexer_path = ROOT_DIR / "scripts" / "indexer.py"
            subprocess.run(["python", str(indexer_path)], capture_output=True)
            
            # Add log entry
            log_path = WIKI_DIR / "log.md"
            curr_date = datetime.now().strftime("%Y-%m-%d")
            log_entry = f"\n## [{curr_date}] ingest | {title}\n- Approved and published note from drafts queue.\n"
            if log_path.exists():
                with open(log_path, "a", encoding="utf-8") as lf:
                    lf.write(log_entry)
                    
            # Run linter
            linter_path = ROOT_DIR / "scripts" / "linter.py"
            subprocess.run(["python", str(linter_path)], capture_output=True)
            
            self.send_json({
                "status": "success",
                "message": f"Successfully approved draft. Note published to {target}."
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    def handle_reject_draft(self):
        content_length = int(self.headers.get('Content-Length', 0))
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            params = json.loads(body)
            name = params.get("name")
            
            if not name:
                self.send_json({"error": "Parameter 'name' is required"}, 400)
                return
                
            draft_path = DRAFTS_DIR / name
            if draft_path.exists():
                draft_path.unlink()
                
            self.send_json({
                "status": "success",
                "message": f"Successfully rejected draft: {name}"
            })
        except Exception as e:
            self.send_json({"error": str(e)}, 500)

def run_server(port=8000):
    handler = WikiHTTPHandler
    # Bind to localhost
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"=== LLM Wiki Local Server Running ===")
        print(f"URL: http://localhost:{port}")
        print(f"Root: {ROOT_DIR}")
        print(f"Dashboard: {DASHBOARD_DIR}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port)
