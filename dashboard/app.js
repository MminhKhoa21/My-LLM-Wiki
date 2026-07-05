// Constants
const API_BASE = "/api";

// DOM Elements
const noteListEl = document.getElementById("note-list");
const sidebarSearchInput = document.getElementById("sidebar-search");
const btnReindex = document.getElementById("btn-reindex");
const btnRelint = document.getElementById("btn-relint");
const btnRefreshLint = document.getElementById("btn-refresh-lint");
const fileUploader = document.getElementById("file-uploader");
const uploadZone = document.getElementById("upload-zone");
const tabNoteBtn = document.getElementById("tab-note-btn");
const tabSearchBtn = document.getElementById("tab-search-btn");
const lintReportArea = document.getElementById("lint-report-area");
const searchResultsArea = document.getElementById("search-results-area");
const noteContentArea = document.getElementById("note-content-area");
const toastEl = document.getElementById("toast");
const toastMessageEl = document.getElementById("toast-message");

// State variables
let notesData = [];
let network = null;

// Initialization
document.addEventListener("DOMContentLoaded", () => {
    initTabs();
    initUploadZone();
    loadNotes();
    loadGraph();
    
    // Actions
    btnReindex.addEventListener("click", runIndexer);
    btnRelint.addEventListener("click", () => switchTab("lint-tab", runLinter));
    btnRefreshLint.addEventListener("click", runLinter);
    
    // Search on enter key
    sidebarSearchInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            const query = sidebarSearchInput.value.trim();
            if (query) {
                switchTab("search-tab", () => runSearch(query));
            }
        }
    });
});

// Toast notification helper
function showToast(message, isError = false) {
    toastMessageEl.innerText = message;
    toastEl.style.borderColor = isError ? "#ef4444" : "var(--secondary)";
    toastEl.classList.add("show");
    
    setTimeout(() => {
        toastEl.classList.remove("show");
    }, 3500);
}

// 1. Tabs management
function initTabs() {
    const tabButtons = document.querySelectorAll(".tab-btn");
    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const tabId = btn.getAttribute("data-tab");
            switchTab(tabId);
        });
    });
}

function switchTab(tabId, callback = null) {
    // Deactivate all buttons and contents
    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".tab-content").forEach(content => content.classList.remove("active"));
    
    // Activate target
    const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
    const content = document.getElementById(tabId);
    
    if (btn) btn.classList.add("active");
    if (content) content.classList.add("active");
    
    if (callback) callback();
}

// 2. Fetch and render note list
async function loadNotes() {
    try {
        const res = await fetch(`${API_BASE}/notes`);
        if (!res.ok) throw new Error("Failed to load notes");
        notesData = await res.json();
        
        renderNoteList(notesData);
    } catch (err) {
        noteListEl.innerHTML = `<li class="error-item">Failed to load notes</li>`;
        showToast(err.message, true);
    }
}

function renderNoteList(notes) {
    if (notes.length === 0) {
        noteListEl.innerHTML = `<li class="empty-item">No notes found. Ingest files to start!</li>`;
        return;
    }
    
    // Sort notes: Overviews first, then alphabetically
    const sorted = [...notes].sort((a, b) => {
        if (a.type === "overview" && b.type !== "overview") return -1;
        if (a.type !== "overview" && b.type === "overview") return 1;
        return a.title.localeCompare(b.title);
    });
    
    noteListEl.innerHTML = sorted.map(note => {
        const date = note.timestamp ? note.timestamp : "";
        return `
            <li class="note-item" data-name="${note.name}">
                <div class="note-title">
                    <i class="fa-solid fa-file-invoice"></i> ${note.title}
                </div>
                <div class="note-desc">${note.description}</div>
                <div class="note-meta">
                    <span class="note-type-badge type-${note.type}">${note.type}</span>
                    <span style="font-size: 10px; color: var(--text-muted);">${date}</span>
                </div>
            </li>
        `;
    }).join("");
    
    // Add click listeners
    document.querySelectorAll(".note-item").forEach(item => {
        item.addEventListener("click", () => {
            const name = item.getAttribute("data-name");
            loadNoteDetail(name);
        });
    });
}

// 3. Load note details & parse Markdown
async function loadNoteDetail(noteName) {
    try {
        // Highlight in sidebar list
        document.querySelectorAll(".note-item").forEach(item => {
            if (item.getAttribute("data-name") === noteName) {
                item.classList.add("active");
            } else {
                item.classList.remove("active");
            }
        });

        // Switch to note view tab
        switchTab("note-tab");
        
        noteContentArea.innerHTML = `<div class="note-viewer-empty"><i class="fa-solid fa-spinner fa-spin empty-icon"></i><p>Reading note contents...</p></div>`;
        
        const res = await fetch(`${API_BASE}/note?name=${encodeURIComponent(noteName)}`);
        if (!res.ok) throw new Error(`Failed to load note: ${noteName}`);
        const data = await res.json();
        
        renderNoteMarkdown(data);
    } catch (err) {
        noteContentArea.innerHTML = `<div class="note-viewer-empty"><i class="fa-solid fa-triangle-exclamation empty-icon" style="color: #ef4444;"></i><p>${err.message}</p></div>`;
        showToast(err.message, true);
    }
}

function renderNoteMarkdown(data) {
    const rawMarkdown = data.markdown;
    
    // Parse double bracket wikilinks: [[note_name]] or [[note_name|Display Text]]
    // E.g., [[isaac_newton]] -> <a href="#" class="wikilink" data-target="isaac_newton">Isaac Newton</a>
    // E.g., [[differentiation_rules|Rules]] -> <a href="#" class="wikilink" data-target="differentiation_rules">Rules</a>
    let parsedMarkdown = rawMarkdown.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (match, target, alias) => {
        const cleanTarget = target.trim();
        const displayLabel = alias ? alias.trim() : cleanTarget.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
        return `<a href="#" class="wikilink" data-target="${cleanTarget}">${displayLabel}</a>`;
    });

    // Custom marked renderer to support links nicely
    const htmlContent = marked.parse(parsedMarkdown);
    
    // Create view container
    noteContentArea.innerHTML = `
        <article class="markdown-body">
            <div style="margin-bottom: 20px; display: flex; gap: 8px; align-items: center; border-bottom: 1px solid var(--panel-border); padding-bottom: 12px;">
                <span class="note-type-badge type-${data.meta.type || 'concept'}">${data.meta.type || 'concept'}</span>
                <span style="font-size: 12px; color: var(--text-muted);"><i class="fa-regular fa-clock"></i> Updated: ${data.meta.timestamp || 'N/A'}</span>
            </div>
            ${htmlContent}
        </article>
    `;
    
    // Add event listeners to interlinked wikilinks inside the rendered note
    noteContentArea.querySelectorAll(".wikilink").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = link.getAttribute("data-target");
            loadNoteDetail(target);
        });
    });
}

// 4. Force-directed Graph Rendering using Vis.js
async function loadGraph() {
    try {
        const res = await fetch(`${API_BASE}/graph`);
        if (!res.ok) throw new Error("Failed to load graph data");
        const data = await res.json();
        
        renderGraph(data);
    } catch (err) {
        showToast(err.message, true);
    }
}

function renderGraph(data) {
    const container = document.getElementById("network-graph");
    
    // Map group types to neon colors
    const colors = {
        overview: { background: "#78350f", border: "#f59e0b", highlight: { background: "#fbbf24", border: "#f59e0b" } },
        summary: { background: "#064e3b", border: "#10b981", highlight: { background: "#34d399", border: "#10b981" } },
        concept: { background: "#0c4a6e", border: "#06b6d4", highlight: { background: "#67e8f9", border: "#06b6d4" } },
        entity: { background: "#4c1d95", border: "#8b5cf6", highlight: { background: "#c084fc", border: "#8b5cf6" } },
        system: { background: "#1e293b", border: "#475569", highlight: { background: "#64748b", border: "#475569" } }
    };
    
    // Process nodes
    const nodes = data.nodes.map(node => {
        const c = colors[node.group] || colors.concept;
        return {
            id: node.id,
            label: node.label,
            color: {
                background: c.background,
                border: c.border,
                highlight: c.highlight
            },
            font: { color: "#f8fafc", face: "Plus Jakarta Sans", size: 14 },
            shape: node.group === "system" ? "box" : "dot",
            size: node.group === "overview" ? 22 : 16,
            borderWidth: 2
        };
    });
    
    // Setup datasets
    const graphData = {
        nodes: new vis.DataSet(nodes),
        edges: new vis.DataSet(data.edges)
    };
    
    // Layout options
    const options = {
        nodes: {
            scaling: { min: 10, max: 30 }
        },
        edges: {
            color: { color: "rgba(255, 255, 255, 0.15)", highlight: "rgba(99, 102, 241, 0.6)" },
            arrows: { to: { enabled: true, scaleFactor: 0.5 } },
            width: 1.5,
            smooth: { type: "continuous" }
        },
        physics: {
            barnesHut: {
                gravitationalConstant: -3000,
                centralGravity: 0.3,
                springLength: 120,
                springConstant: 0.04
            },
            stabilization: { iterations: 150 }
        },
        interaction: {
            hover: true,
            tooltipDelay: 200
        }
    };
    
    // Create network
    network = new vis.Network(container, graphData, options);
    
    // Double click or click event
    network.on("selectNode", (params) => {
        const nodeId = params.nodes[0];
        if (nodeId) {
            loadNoteDetail(nodeId);
        }
    });
}

// 5. Ingestion & Re-indexing
async function runIndexer() {
    try {
        btnReindex.disabled = true;
        btnReindex.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Rebuilding...`;
        
        const res = await fetch(`${API_BASE}/run-indexer`, { method: "POST" });
        if (!res.ok) throw new Error("Indexer failed");
        const data = await res.json();
        
        showToast(data.message || "Index rebuilt successfully!");
        
        // Reload list and graph
        await loadNotes();
        await loadGraph();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnReindex.disabled = false;
        btnReindex.innerHTML = `<i class="fa-solid fa-list-check"></i> Rebuild Index`;
    }
}

// 6. Linter Status check
async function runLinter() {
    try {
        btnRelint.disabled = true;
        btnRefreshLint.disabled = true;
        lintReportArea.innerHTML = `<div style="text-align: center; padding: 40px;"><i class="fa-solid fa-spinner fa-spin fa-2xl"></i><p style="margin-top: 15px;">Scanning repository files...</p></div>`;
        
        const res = await fetch(`${API_BASE}/lint`);
        if (!res.ok) throw new Error("Linter execution failed");
        const data = await res.json();
        
        // Render report
        lintReportArea.innerHTML = data.report;
        showToast("Wiki health check complete!");
    } catch (err) {
        lintReportArea.innerHTML = `<p style="color: #ef4444;">Error running health check: ${err.message}</p>`;
        showToast(err.message, true);
    } finally {
        btnRelint.disabled = false;
        btnRefreshLint.disabled = false;
    }
}

// 7. Keyword Search query
async function runSearch(query) {
    try {
        searchResultsArea.innerHTML = `<div style="text-align: center; padding: 40px;"><i class="fa-solid fa-spinner fa-spin fa-2xl"></i><p style="margin-top: 15px;">Searching matching files...</p></div>`;
        
        const res = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        if (!res.ok) throw new Error("Search execution failed");
        const data = await res.json();
        
        searchResultsArea.innerHTML = data.results;
    } catch (err) {
        searchResultsArea.innerHTML = `<p style="color: #ef4444;">Error running search: ${err.message}</p>`;
        showToast(err.message, true);
    }
}

// 8. Raw File Drag & Drop upload
function initUploadZone() {
    // Click to upload
    uploadZone.addEventListener("click", () => fileUploader.click());
    
    fileUploader.addEventListener("change", () => {
        if (fileUploader.files.length > 0) {
            uploadFile(fileUploader.files[0]);
        }
    });
    
    // Drag & drop events
    uploadZone.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadZone.style.borderColor = "var(--secondary)";
        uploadZone.style.background = "rgba(6, 182, 212, 0.08)";
    });
    
    uploadZone.addEventListener("dragleave", () => {
        uploadZone.style.borderColor = "var(--panel-border)";
        uploadZone.style.background = "transparent";
    });
    
    uploadZone.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadZone.style.borderColor = "var(--panel-border)";
        uploadZone.style.background = "transparent";
        
        if (e.dataTransfer.files.length > 0) {
            uploadFile(e.dataTransfer.files[0]);
        }
    });
}

async function uploadFile(file) {
    try {
        showToast(`Uploading: ${file.name}...`);
        
        const res = await fetch(`${API_BASE}/upload`, {
            method: "POST",
            headers: {
                "File-Name": file.name,
                "Content-Type": "application/octet-stream"
            },
            body: file
        });
        
        if (!res.ok) throw new Error("Upload failed");
        const data = await res.json();
        
        showToast(data.message || "File uploaded successfully!");
    } catch (err) {
        showToast(err.message, true);
    }
}
