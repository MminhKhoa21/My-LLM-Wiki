import os
import sys
import json
import urllib.request
import urllib.error
import re
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
RAW_DIR = ROOT_DIR / "raw"
ENV_PATH = ROOT_DIR / ".env"

def load_env():
    env_vars = {}
    if ENV_PATH.exists():
        try:
            with open(ENV_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        env_vars[k.strip()] = v.strip()
        except Exception as e:
            print(f"[WARN] Failed to read .env: {e}")
    return env_vars

def call_llm(text_a, name_a, text_b, name_b, env_vars):
    # Determine API configurations
    api_key = env_vars.get("DEEPSEEK_API_KEY")
    api_url = env_vars.get("DEEPSEEK_API_URL", "https://api.deepseek.com").rstrip("/") + "/chat/completions"
    model = env_vars.get("DEEPSEEK_MODEL", "deepseek-chat")
    
    if not api_key:
        api_key = env_vars.get("MISTRAL_API_KEY")
        api_url = "https://api.mistral.ai/v1/chat/completions"
        model = env_vars.get("MISTRAL_MODEL", "mistral-tiny")
        
    if not api_key:
        raise ValueError("No API Key found for DeepSeek or Mistral. Set them in .env file.")

    system_prompt = (
        "You are a logical validation engine.\n"
        "Analyze the two texts provided and check if they contain any direct factual contradictions or logical inconsistencies.\n"
        "Respond strictly in JSON format with the following keys:\n"
        "{\n"
        "  \"contradiction_found\": true/false,\n"
        "  \"explanation\": \"Clear explanation of the factual conflict if found, else empty\",\n"
        "  \"claim_a\": \"The claim made in Text A that conflicts\",\n"
        "  \"claim_b\": \"The claim made in Text B that conflicts\"\n"
        "}"
    )

    prompt = (
        f"Compare these two sources for factual contradictions:\n\n"
        f"--- Text A (Source: {name_a}) ---\n"
        f"{text_a[:3000]}\n\n"
        f"--- Text B (Source: {name_b}) ---\n"
        f"{text_b[:3000]}\n"
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    }
    
    # Mistral tiny or older models might not support JSON response format parameter, 
    # but DeepSeek does. We add it conditionally.
    if "deepseek" in model.lower():
        payload["response_format"] = {"type": "json_object"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(api_url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as response:
            res_body = response.read().decode("utf-8")
            res_data = json.loads(res_body)
            content = res_data["choices"][0]["message"]["content"]
            # Clean possible markdown wrapping
            if content.startswith("```json"):
                content = content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"API Error ({e.code}): {err_msg}")
    except Exception as e:
        raise RuntimeError(f"HTTP Connection failed: {e}")

def parse_frontmatter(content):
    frontmatter = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        for line in yaml_content.split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip()
                # Parse list or basic strings
                if v.startswith("[") and v.endswith("]"):
                    v = [item.strip().strip('"').strip("'") for item in v[1:-1].split(",") if item.strip()]
                else:
                    v = v.strip('"').strip("'")
                frontmatter[k] = v
    return frontmatter

def strip_frontmatter(content):
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)

def apply_contradiction_warning(file_path, explanation, claim_a, name_a, claim_b, name_b):
    if not file_path.exists():
        return
        
    content = file_path.read_text(encoding="utf-8")
    
    # Check if warning already exists
    if "> [!WARNING] AI Contradiction Detected" in content:
        return
        
    # Construct the warning box
    warning_box = (
        f"> [!WARNING] AI Contradiction Detected\n"
        f"> **Conflict:** {explanation}\n"
        f"> - **Source {name_a}:** \"{claim_a}\"\n"
        f"> - **Source {name_b}:** \"{claim_b}\"\n\n"
    )
    
    # Insert right below frontmatter
    match = re.match(r"^(---\s*\n.*?\n---\s*\n)", content, re.DOTALL)
    if match:
        end_frontmatter = match.end(1)
        new_content = content[:end_frontmatter] + warning_box + content[end_frontmatter:]
    else:
        new_content = warning_box + content
        
    file_path.write_text(new_content, encoding="utf-8")
    print(f"[CONTRADITION] Warning alert added to {file_path.name}")

def log_contradiction(note_name, explanation):
    log_path = WIKI_DIR / "log.md"
    if log_path.exists():
        try:
            curr_date = datetime.now().strftime("%Y-%m-%d")
            log_content = log_path.read_text(encoding="utf-8")
            log_entry = (
                f"\n\n## [{curr_date}] contradiction | Factual conflict in [[{note_name}]]\n"
                f"- **Conflict details:** {explanation}\n"
                f"- Automatically logged by contradiction_checker.py"
            )
            log_path.write_text(log_content + log_entry, encoding="utf-8")
            print(f"[CONTRADITION] Event logged in wiki/log.md")
        except Exception as e:
            print(f"[WARN] Failed to write log: {e}")

def run_contradiction_check(target_file=None, mock_mode=False):
    env_vars = load_env()
    
    if not mock_mode and not env_vars.get("DEEPSEEK_API_KEY") and not env_vars.get("MISTRAL_API_KEY"):
        print("[SKIP] Contradiction check skipped. Mistral/DeepSeek API keys are not set in .env")
        return []
        
    warnings = []
    
    # Collect files to scan
    files_to_scan = []
    if target_file:
        p = Path(target_file)
        if p.exists() and p.is_file():
            files_to_scan.append(p)
    else:
        # Scan all generated wiki pages
        for p in WIKI_DIR.glob("*.md"):
            if p.name not in ["index.md", "log.md", "overview.md"]:
                files_to_scan.append(p)
                
    if not files_to_scan:
        print("[OK] No wiki files found to analyze.")
        return []
        
    print(f"=== Running Semantic Contradiction Check (Mock: {mock_mode}) ===")
    
    if mock_mode:
        # Simulate finding a contradiction on the first note
        test_file = files_to_scan[0]
        name = test_file.stem
        explanation = "Mock contradiction: Text conflicts on dates/attribution claims."
        claim_a = "Isaac Newton discovered calculus in 1665."
        claim_b = "Gottfried Leibniz invented calculus independently in 1675."
        
        apply_contradiction_warning(test_file, explanation, claim_a, "Newton Bio", claim_b, "Leibniz Bio")
        log_contradiction(name, explanation)
        warnings.append({
            "file": test_file.name,
            "explanation": explanation
        })
        return warnings

    # Real LLM check
    for file_path in files_to_scan:
        try:
            content = file_path.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            sources = fm.get("sources", [])
            
            if not sources:
                continue
                
            clean_note_text = strip_frontmatter(content)
            
            for src in sources:
                src_path = ROOT_DIR / src
                if not src_path.exists() or not src_path.is_file():
                    # Check if external URL or missing
                    continue
                    
                src_text = src_path.read_text(encoding="utf-8")
                
                print(f"Comparing [[{file_path.stem}]] with source '{src}'...")
                res = call_llm(clean_note_text, file_path.name, src_text, src_path.name, env_vars)
                
                if res.get("contradiction_found"):
                    explanation = res.get("explanation", "Factual conflict detected.")
                    claim_a = res.get("claim_a", "N/A")
                    claim_b = res.get("claim_b", "N/A")
                    
                    print(f"[ALERT] Contradiction found between {file_path.name} and {src_path.name}!")
                    print(f"Detail: {explanation}")
                    
                    apply_contradiction_warning(file_path, explanation, claim_a, file_path.name, claim_b, src_path.name)
                    log_contradiction(file_path.stem, explanation)
                    warnings.append({
                        "file": file_path.name,
                        "explanation": explanation
                    })
                    break # Stop check on this note after first conflict
        except Exception as e:
            print(f"[ERROR] Failed checking {file_path.name}: {e}")
            
    return warnings

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to specific wiki file to check")
    parser.add_argument("--mock", action="store_true", help="Simulate a contradiction check for verification")
    args = parser.parse_args()
    
    run_contradiction_check(args.file, args.mock)
