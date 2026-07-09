// Constants
const API_BASE = "/api";

// Translations
const translations = {
    en: {
        "logo-title": "LLM Wiki",
        "search-placeholder": "Quick search...",
        "section-wiki": "Wiki Pages",
        "loading-notes": "Loading notes...",
        "section-actions": "Quick Actions",
        "action-reindex": "Rebuild Index",
        "action-relint": "Check Health",
        "action-upload": "Drop new raw source or click",
        "tab-graph": "Knowledge Graph",
        "tab-note": "Note Viewer",
        "tab-lint": "Health Report",
        "tab-search": "Search Results",
        "tab-manage": "Manage Notes",
        "graph-title": "Interactive Knowledge Network",
        "graph-subtitle": "Click on notes to browse their contents",
        "note-empty": "Select a note from the sidebar or click a node in the graph view to inspect it.",
        "lint-title": "Linter Status Report",
        "lint-btn": "Run Health Check",
        "lint-empty": "Click \"Run Health Check\" to scan the repository for schema violations, broken links, and orphans.",
        "search-title": "Query Search Matches",
        "search-empty": "Search query matches will appear here. Enter a query in the sidebar search box to search.",
        "manage-title": "Lesson & File Management",
        "manage-subtitle": "Delete and manage raw sources and generated wiki pages",
        "manage-wiki-header": "Wiki Pages (.md)",
        "manage-raw-header": "Raw Sources (immutability rule)",
        "lbl-core": "System Core (Blocked)",
        "lbl-wiki-page": "Wiki Page (Deletable)",
        "lbl-raw-src": "Raw Source (Deletable)",
        "btn-delete": "Delete",
        "toast-deleted": "File deleted successfully!",
        "toast-delete-fail": "Failed to delete file: ",
        "confirm-delete": "Are you sure you want to delete this file?",
        "clip-placeholder": "Paste article URL...",
        "action-clip": "Clip & Ingest",
        "toast-clipping": "Clipping website...",
        "toast-clip-success": "Successfully clipped: ",
        "toast-clip-fail": "Failed to clip webpage: ",
        "tab-drafts": "Review Drafts",
        "recent-title": "Recent Updates",
        "drafts-title": "AI Proposed Drafts",
        "drafts-subtitle": "Review, edit, and approve AI-generated wiki articles",
        "drafts-pending-hdr": "Pending Review",
        "draft-editor-empty-msg": "Select a draft from the queue to review and approve.",
        "btn-reject": "Reject",
        "btn-approve": "Approve & Publish",
        "toast-draft-approved": "Draft approved and published!",
        "toast-draft-rejected": "Draft rejected and deleted.",
        "toast-draft-loading": "AI analyzing raw sources... Drafts will appear in Review Drafts tab shortly.",
        "btn-reject-all": "Reject All",
        "btn-approve-all": "Approve All",
        "toast-drafts-approved-all": "Approved and published all drafts!",
        "toast-drafts-rejected-all": "Rejected and deleted all drafts.",
        "tab-report": "Quick Report",
        "report-title": "GitHub Repo Quick Report",
        "report-subtitle": "Paste a GitHub link to generate a Vietnamese AI analysis report",
        "report-placeholder": "https://github.com/owner/repo",
        "btn-generate-report": "Generate Report",
        "btn-download-report": "Download HTML",
        "btn-print-report": "Print / PDF",
        "report-history": "Saved Reports",
        "toast-report-generating": "Analyzing repository... This may take 30-60 seconds.",
        "toast-report-done": "Report generated successfully!",
        "toast-report-fail": "Failed to generate report: "
    },
    vi: {
        "logo-title": "LLM Wiki",
        "search-placeholder": "Tìm kiếm nhanh...",
        "section-wiki": "Danh sách Bài học",
        "loading-notes": "Đang tải dữ liệu...",
        "section-actions": "Thao tác nhanh",
        "action-reindex": "Cập nhật Mục lục",
        "action-relint": "Kiểm tra sức khỏe",
        "action-upload": "Kéo thả tài liệu nguồn vào đây",
        "tab-graph": "Đồ thị tri thức",
        "tab-note": "Nội dung bài học",
        "tab-lint": "Báo cáo sức khỏe",
        "tab-search": "Kết quả tìm kiếm",
        "tab-manage": "Quản lý bài học",
        "graph-title": "Đồ thị tri thức tương tác",
        "graph-subtitle": "Click vào các ghi chú để xem nội dung",
        "note-empty": "Chọn một bài học ở thanh bên hoặc click vào nút đồ thị để xem nội dung chi tiết.",
        "lint-title": "Báo cáo chi tiết sức khỏe Wiki",
        "lint-btn": "Bắt đầu kiểm tra",
        "lint-empty": "Nhấn \"Bắt đầu kiểm tra\" để rà soát lỗi cấu trúc frontmatter, liên kết hỏng hoặc trang mồ côi.",
        "search-title": "Kết quả tìm kiếm từ khóa",
        "search-empty": "Kết quả khớp từ khóa sẽ hiển thị ở đây. Nhập từ khóa tìm kiếm ở thanh bên để tra cứu.",
        "manage-title": "Quản lý Bài học & Tài liệu",
        "manage-subtitle": "Xóa và quản lý các tài liệu nguồn thô cùng các trang wiki đã sinh",
        "manage-wiki-header": "Danh sách trang Wiki (.md)",
        "manage-raw-header": "Tài liệu nguồn thô (Nguyên tắc bất biến)",
        "lbl-core": "Không được xóa (Hệ thống)",
        "lbl-wiki-page": "Có thể xóa (Trang Wiki)",
        "lbl-raw-src": "Có thể xóa (Nguồn thô)",
        "btn-delete": "Xóa",
        "toast-deleted": "Đã xóa file thành công!",
        "toast-delete-fail": "Lỗi khi xóa file: ",
        "confirm-delete": "Bạn có chắc chắn muốn xóa tệp này không?",
        "clip-placeholder": "Dán liên kết URL bài báo...",
        "action-clip": "Tải bài viết",
        "toast-clipping": "Đang tải bài viết...",
        "toast-clip-success": "Tải bài viết thành công: ",
        "toast-clip-fail": "Lỗi khi tải bài viết: ",
        "tab-drafts": "Duyệt bản thảo",
        "recent-title": "Bài học mới cập nhật",
        "drafts-title": "Bản thảo AI đề xuất",
        "drafts-subtitle": "Rà soát, chỉnh sửa và phê duyệt các bài học do AI biên soạn",
        "drafts-pending-hdr": "Chờ phê duyệt",
        "draft-editor-empty-msg": "Chọn một bản thảo ở hàng đợi để tiến hành rà soát và phê duyệt.",
        "btn-reject": "Từ chối",
        "btn-approve": "Duyệt & Xuất bản",
        "toast-draft-approved": "Đã phê duyệt và xuất bản bài viết!",
        "toast-draft-rejected": "Đã từ chối và xóa bản thảo.",
        "toast-draft-loading": "AI đang phân tích tài liệu thô... Bản thảo đề xuất sẽ xuất hiện trong tab Duyệt Bản Thảo sớm.",
        "btn-reject-all": "Xóa tất cả",
        "btn-approve-all": "Duyệt tất cả",
        "toast-drafts-approved-all": "Đã duyệt và xuất bản tất cả bản thảo!",
        "toast-drafts-rejected-all": "Đã từ chối và xóa sạch hàng đợi bản thảo.",
        "tab-report": "Báo cáo nhanh",
        "report-title": "Báo cáo nhanh GitHub Repo",
        "report-subtitle": "Dán link GitHub để AI tự động phân tích và tạo báo cáo bằng Tiếng Việt",
        "report-placeholder": "https://github.com/owner/repo",
        "btn-generate-report": "Tạo báo cáo",
        "btn-download-report": "Tải xuống HTML",
        "btn-print-report": "In / PDF",
        "report-history": "Báo cáo đã lưu",
        "toast-report-generating": "Đang phân tích repo... Quá trình này có thể mất 30-60 giây.",
        "toast-report-done": "Tạo báo cáo thành công!",
        "toast-report-fail": "Lỗi khi tạo báo cáo: "
    }
};

let currentLang = "vi";
let currentNoteName = null;
let sortedNotes = [];

// DOM Elements
const noteListEl = document.getElementById("note-list");
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
const btnLangToggle = document.getElementById("btn-lang-toggle");
const manageWikiListEl = document.getElementById("manage-wiki-list");
const manageRawListEl = document.getElementById("manage-raw-list");
const clipperUrlInput = document.getElementById("clipper-url");
const btnClip = document.getElementById("btn-clip");
const gitStatusBadge = document.getElementById("git-status-badge");
const gitControls = document.getElementById("git-controls");
const gitCommitMsgInput = document.getElementById("git-commit-msg");
const btnGitCommit = document.getElementById("btn-git-commit");
const noteViewerHeader = document.querySelector(".note-viewer-header");
const noteViewerTitle = document.getElementById("note-viewer-title");
const btnCopyObsidian = document.getElementById("btn-copy-obsidian");
const btnCleanupRaw = document.getElementById("btn-cleanup-raw");
const topSearchInput = document.getElementById("top-search");
const topSearchResults = document.getElementById("top-search-results");
const recentUpdatesList = document.getElementById("recent-updates-list");
const draftsCountBadge = document.getElementById("drafts-count-badge");
const draftsListEl = document.getElementById("drafts-list");
const draftEditorEmpty = document.getElementById("draft-editor-empty");
const draftEditorContent = document.getElementById("draft-editor-content");
const draftReviewTitle = document.getElementById("draft-review-title");
const draftEditorTextarea = document.getElementById("draft-editor-textarea");
const btnApproveDraft = document.getElementById("btn-approve-draft");
const btnRejectDraft = document.getElementById("btn-reject-draft");
const btnApproveAll = document.getElementById("btn-approve-all");
const btnRejectAll = document.getElementById("btn-reject-all");
// State variables
let notesData = [];
let network = null;
let rawGraphData = null;
let activeGraphFilters = { overview: true, summary: true, concept: true, entity: true, system: true };
let activeDrafts = [];
let currentDraftName = null;

// Configuration & Security Check
async function checkConfig() {
    try {
        const res = await fetch(`${API_BASE}/config`);
        if (!res.ok) return;
        const config = await res.json();
        if (config.readOnly) {
            document.body.classList.add("read-only-mode");
            const elementsToHide = [
                document.getElementById("btn-reindex"),
                document.getElementById("btn-relint"),
                document.querySelector(".clipper-area"),
                document.getElementById("upload-zone"),
                document.getElementById("git-controls"),
                document.getElementById("tab-manage-btn"),
                document.getElementById("tab-drafts-btn"),
                document.getElementById("btn-cleanup-raw")
            ];
            elementsToHide.forEach(el => {
                if (el) el.style.display = "none";
            });
            const uploadArea = document.querySelector(".upload-area");
            if (uploadArea) {
                uploadArea.innerHTML = '<span style="color: var(--text-muted); font-size: 11px; text-align: center; display: block; padding: 10px;">Chế độ Xem (Read-only)</span>';
                uploadArea.style.pointerEvents = "none";
                uploadArea.style.borderStyle = "solid";
            }
        }
    } catch (err) {
        console.error("Failed to load config", err);
    }
}

// Initialization
document.addEventListener("DOMContentLoaded", () => {
    checkConfig();
    initTabs();
    initUploadZone();
    loadNotes();
    loadGraph();
    updateLanguageUI();
    checkGitStatus();
    initGraphFilters();
    loadRecentUpdates();
    loadDrafts();
    
    // Actions
    btnReindex.addEventListener("click", runIndexer);
    btnRelint.addEventListener("click", () => switchTab("lint-tab", runLinter));
    btnRefreshLint.addEventListener("click", runLinter);
    btnLangToggle.addEventListener("click", toggleLanguage);
    btnClip.addEventListener("click", runWebClipper);
    btnGitCommit.addEventListener("click", commitGitChanges);
    btnCopyObsidian.addEventListener("click", copyObsidianLink);
    btnCleanupRaw.addEventListener("click", cleanupRawSources);
    btnApproveDraft.addEventListener("click", approveCurrentDraft);
    btnRejectDraft.addEventListener("click", rejectCurrentDraft);
    btnApproveAll.addEventListener("click", approveAllDrafts);
    btnRejectAll.addEventListener("click", rejectAllDrafts);
    // Top Search listeners
    topSearchInput.addEventListener("input", handleTopSearchInput);
    document.addEventListener("click", (e) => {
        if (!topSearchInput.contains(e.target) && !topSearchResults.contains(e.target)) {
            topSearchResults.style.display = "none";
        }
    });

    // Mobile Menu Toggle
    const btnMobileMenu = document.getElementById("btn-mobile-menu");
    const sidebar = document.getElementById("sidebar");
    const mobileOverlay = document.getElementById("mobile-overlay");
    
    function toggleMobileMenu() {
        sidebar.classList.toggle("open");
        mobileOverlay.classList.toggle("active");
    }
    
    if (btnMobileMenu && sidebar && mobileOverlay) {
        btnMobileMenu.addEventListener("click", toggleMobileMenu);
        mobileOverlay.addEventListener("click", toggleMobileMenu);
        
        // Close menu automatically when clicking a note item in sidebar on mobile
        sidebar.addEventListener("click", (e) => {
            if (window.innerWidth <= 768 && (e.target.closest('.note-item') || e.target.closest('.recent-item') || e.target.closest('.btn'))) {
                sidebar.classList.remove("open");
                mobileOverlay.classList.remove("active");
            }
        });
    }
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
            switchTab(tabId, () => {
                if (tabId === "manage-tab") {
                    loadManagementData();
                } else if (tabId === "drafts-tab") {
                    loadDrafts();
                }
            });
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
        const res = await fetch(`${API_BASE}/notes?lang=${currentLang}`);
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
    
    // Helper to extract day and track for natural sorting
    function parseLessonKey(name) {
        const dayMatch = name.match(/day(\d+)/i);
        const day = dayMatch ? parseInt(dayMatch[1], 10) : 999;
        const trackMatch = name.match(/track(\d+)/i);
        // Overviews have no track, assign them track 0
        const track = trackMatch ? parseInt(trackMatch[1], 10) : 0;
        return { day, track };
    }

    // Sort notes: Group by Track (0 = Overview, 1 = Track 1, etc.), then by Day
    sortedNotes = [...notes].sort((a, b) => {
        const keyA = parseLessonKey(a.name);
        const keyB = parseLessonKey(b.name);
        if (keyA.track !== keyB.track) return keyA.track - keyB.track;
        if (keyA.day !== keyB.day) return keyA.day - keyB.day;
        return a.title.localeCompare(b.title);
    });
    
    noteListEl.innerHTML = sortedNotes.map(note => {
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
        
        noteContentArea.classList.add("note-viewer-empty");
        noteContentArea.innerHTML = `<div class="note-viewer-empty"><i class="fa-solid fa-spinner fa-spin empty-icon"></i><p>Reading note contents...</p></div>`;
        noteViewerHeader.style.display = "none";
        
        currentNoteName = noteName;
        const res = await fetch(`${API_BASE}/note?name=${encodeURIComponent(noteName)}&lang=${currentLang}`);
        if (!res.ok) throw new Error(`Failed to load note: ${noteName}`);
        const data = await res.json();
        
        // Show and configure header
        noteViewerTitle.innerText = data.meta.title || noteName;
        btnCopyObsidian.setAttribute("data-file", noteName);
        noteViewerHeader.style.display = "flex";
        
        renderNoteMarkdown(data);
        
        // Navigation Buttons logic
        const currentIndex = sortedNotes.findIndex(n => n.name === noteName);
        const navContainer = document.getElementById("note-navigation");
        const prevBtn = document.getElementById("btn-prev-note");
        const nextBtn = document.getElementById("btn-next-note");
        
        if (currentIndex !== -1 && sortedNotes.length > 1) {
            navContainer.style.display = "flex";
            
            if (currentIndex > 0) {
                const prevNote = sortedNotes[currentIndex - 1];
                prevBtn.style.display = "inline-block";
                prevBtn.onclick = () => loadNoteDetail(prevNote.name);
                prevBtn.title = prevNote.title;
            } else {
                prevBtn.style.display = "none";
            }
            
            if (currentIndex < sortedNotes.length - 1) {
                const nextNote = sortedNotes[currentIndex + 1];
                nextBtn.style.display = "inline-block";
                nextBtn.onclick = () => loadNoteDetail(nextNote.name);
                nextBtn.title = nextNote.title;
            } else {
                nextBtn.style.display = "none";
            }
        } else {
            navContainer.style.display = "none";
        }
    } catch (err) {
        document.getElementById("note-navigation").style.display = "none";
        noteViewerHeader.style.display = "none";
        noteContentArea.classList.add("note-viewer-empty");
        noteContentArea.innerHTML = `<div class="note-viewer-empty"><i class="fa-solid fa-triangle-exclamation empty-icon" style="color: #ef4444;"></i><p>${err.message}</p></div>`;
        showToast(err.message, true);
    }
}

function renderNoteMarkdown(data) {
    const rawMarkdown = data.markdown;
    
    // Parse double bracket wikilinks
    let parsedMarkdown = rawMarkdown.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (match, target, alias) => {
        const cleanTarget = target.trim();
        const displayLabel = alias ? alias.trim() : cleanTarget.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
        return `<a href="#" class="wikilink" data-target="${cleanTarget}">${displayLabel}</a>`;
    });

    // Parse Obsidian callouts
    parsedMarkdown = parsedMarkdown.replace(/(?:^|\n)> \[!(\w+)\](.*)(?:\n>.*)*/gi, (match) => {
        const lines = match.trim().split('\n');
        const headerMatch = lines[0].match(/> \[!(\w+)\](.*)/i);
        const type = headerMatch[1].toLowerCase();
        const title = headerMatch[2].trim() || type.toUpperCase();
        
        const contentLines = lines.slice(1).map(l => l.replace(/^>\s?/, '')).join('\n');
        
        let icon = "fa-circle-info";
        if (type === "warning") icon = "fa-triangle-exclamation";
        else if (type === "important" || type === "danger") icon = "fa-circle-exclamation";
        else if (type === "success" || type === "check") icon = "fa-circle-check";
        
        return `
<div class="callout callout-${type}">
<div class="callout-title"><i class="fa-solid ${icon}"></i> ${title}</div>
<div class="callout-content">

${contentLines}

</div>
</div>
`;
    });

    const htmlContent = marked.parse(parsedMarkdown);
    
    noteContentArea.classList.remove("note-viewer-empty");
    noteContentArea.innerHTML = `
        <article class="markdown-body">
            <div style="margin-bottom: 20px; display: flex; gap: 8px; align-items: center; border-bottom: 1px solid var(--panel-border); padding-bottom: 12px;">
                <span class="note-type-badge type-${data.meta.type || 'concept'}">${data.meta.type || 'concept'}</span>
                <span style="font-size: 12px; color: var(--text-muted);"><i class="fa-regular fa-clock"></i> Updated: ${data.meta.timestamp || 'N/A'}</span>
            </div>
            ${htmlContent}
        </article>
    `;
    
    // Add event listeners to interlinked wikilinks
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
        const res = await fetch(`${API_BASE}/graph?lang=${currentLang}`);
        if (!res.ok) throw new Error("Failed to load graph data");
        const data = await res.json();
        
        renderGraph(data);
    } catch (err) {
        showToast(err.message, true);
    }
}

function renderGraph(data) {
    const container = document.getElementById("network-graph");
    rawGraphData = data;
    
    // Map group types to neon colors
    const colors = {
        overview: { background: "#78350f", border: "#f59e0b", highlight: { background: "#fbbf24", border: "#f59e0b" } },
        summary: { background: "#064e3b", border: "#10b981", highlight: { background: "#34d399", border: "#10b981" } },
        concept: { background: "#0c4a6e", border: "#06b6d4", highlight: { background: "#67e8f9", border: "#06b6d4" } },
        entity: { background: "#4c1d95", border: "#8b5cf6", highlight: { background: "#c084fc", border: "#8b5cf6" } },
        system: { background: "#1e293b", border: "#475569", highlight: { background: "#64748b", border: "#475569" } }
    };
    
    // Map connected node IDs to filter out orphan nodes
    const connectedNodeIds = new Set();
    data.edges.forEach(edge => {
        connectedNodeIds.add(edge.from);
        connectedNodeIds.add(edge.to);
    });

    // Process nodes
    const filteredNodes = data.nodes.filter(node => {
        const group = node.group || "concept";
        if (activeGraphFilters[group] === false) return false;
        return connectedNodeIds.has(node.id);
    });
    
    const nodes = filteredNodes.map(node => {
        const c = colors[node.group] || colors.concept;
        return {
            id: node.id,
            label: node.label,
            color: {
                background: c.background,
                border: c.border,
                highlight: c.highlight
            },
            font: { color: "#f8fafc", face: "Plus Jakarta Sans", size: 11 },
            shape: node.group === "system" ? "box" : "dot",
            size: node.group === "overview" ? 12 : 6,
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

// 9. Bilingual Language Switching
function toggleLanguage() {
    currentLang = currentLang === "en" ? "vi" : "en";
    btnLangToggle.innerText = currentLang === "en" ? "VI" : "EN";
    updateLanguageUI();
    // Reload dynamically rendered elements
    loadNotes();
    loadGraph();
    if (document.getElementById("manage-tab").classList.contains("active")) {
        loadManagementData();
    }
    if (currentNoteName && document.getElementById("note-tab").classList.contains("active")) {
        loadNoteDetail(currentNoteName);
    }
}

function updateLanguageUI() {
    const langData = translations[currentLang];
    
    // Translate text contents
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (langData[key]) {
            // Keep child icons if any
            const icon = el.querySelector("i");
            if (icon) {
                el.innerHTML = "";
                el.appendChild(icon);
                el.appendChild(document.createTextNode(" " + langData[key]));
            } else {
                el.innerText = langData[key];
            }
        }
    });
    
    // Translate placeholders
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (langData[key]) {
            el.setAttribute("placeholder", langData[key]);
        }
    });
}

// 10. Lesson / Note Management & Deletion
async function loadManagementData() {
    try {
        manageWikiListEl.innerHTML = `<div style="padding: 15px; color: var(--text-muted);"><i class="fa-solid fa-spinner fa-spin"></i> Loading...</div>`;
        manageRawListEl.innerHTML = `<div style="padding: 15px; color: var(--text-muted);"><i class="fa-solid fa-spinner fa-spin"></i> Loading...</div>`;
        
        // Fetch Wiki pages
        const wikiRes = await fetch(`${API_BASE}/notes?lang=${currentLang}`);
        const wikis = wikiRes.ok ? await wikiRes.json() : [];
        
        // Fetch Raw files
        const rawRes = await fetch(`${API_BASE}/raw-files`);
        const raws = rawRes.ok ? await rawRes.json() : [];
        
        renderManagementWiki(wikis);
        renderManagementRaw(raws);
    } catch (err) {
        showToast("Error loading management data: " + err.message, true);
    }
}

function renderManagementWiki(wikis) {
    const langData = translations[currentLang];
    const allWikis = [
        { name: "overview", title: "Learning Wiki Overview", isSystem: true },
        { name: "index", title: "Wiki Index", isSystem: true },
        { name: "log", title: "Operation Log", isSystem: true },
        ...wikis.map(w => ({ ...w, isSystem: false }))
    ];

    manageWikiListEl.innerHTML = allWikis.map(item => {
        const badgeClass = item.isSystem ? "policy-unsafe" : "policy-safe";
        const badgeLabel = item.isSystem ? langData["lbl-core"] : langData["lbl-wiki-page"];
        const disabled = item.isSystem ? "disabled" : "";
        const titleText = item.title || item.name;
        return `
        <div class="manage-item-row ${item.isSystem ? '' : ''}" data-name="${item.name}.md" data-type="wiki">
            <input type="checkbox" ${disabled} data-cb-wiki onchange="updateWikiBulkBar()">
            <span class="manage-item-label" title="${titleText}">${titleText}<br><small style="color:var(--text-muted);font-size:10px;">${item.name}.md</small></span>
            <span class="policy-badge ${badgeClass}" style="font-size:9px;">${badgeLabel}</span>
            <button class="manage-item-delete" ${disabled} data-type="wiki" data-name="${item.name}.md" title="Delete">
                <i class="fa-solid fa-xmark"></i>
            </button>
        </div>`;
    }).join("");

    manageWikiListEl.querySelectorAll(".manage-item-delete").forEach(btn => {
        btn.addEventListener("click", () => confirmAndDelete("wiki", btn.dataset.name));
    });

    // Select-all checkbox
    const saAll = document.getElementById("wiki-select-all");
    if (saAll) saAll.onchange = () => {
        manageWikiListEl.querySelectorAll("input[data-cb-wiki]:not(:disabled)").forEach(cb => cb.checked = saAll.checked);
        updateWikiBulkBar();
    };
    updateWikiBulkBar();
}

function renderManagementRaw(raws) {
    const langData = translations[currentLang];
    if (raws.length === 0) {
        manageRawListEl.innerHTML = `<div style="padding: 15px; color: var(--text-muted); font-style: italic;">No raw sources found.</div>`;
        return;
    }
    manageRawListEl.innerHTML = raws.map(item => {
        const kbSize = (item.size / 1024).toFixed(1);
        return `
        <div class="manage-item-row" data-name="${item.name}" data-type="raw">
            <input type="checkbox" data-cb-raw onchange="updateRawBulkBar()">
            <span class="manage-item-label" title="${item.name}">${item.name}<br><small style="color:var(--text-muted);font-size:10px;">${kbSize} KB</small></span>
            <button class="manage-item-delete" data-type="raw" data-name="${item.name}" title="Delete">
                <i class="fa-solid fa-xmark"></i>
            </button>
        </div>`;
    }).join("");

    manageRawListEl.querySelectorAll(".manage-item-delete").forEach(btn => {
        btn.addEventListener("click", () => confirmAndDelete("raw", btn.dataset.name));
    });

    const saAll = document.getElementById("raw-select-all");
    if (saAll) saAll.onchange = () => {
        manageRawListEl.querySelectorAll("input[data-cb-raw]").forEach(cb => cb.checked = saAll.checked);
        updateRawBulkBar();
    };
    updateRawBulkBar();
}

function confirmAndDelete(type, name) {
    const langData = translations[currentLang];
    if (confirm(`${langData["confirm-delete"]}\n(${name})`)) {
        deleteFile(type, name);
    }
}

async function deleteFile(type, name) {
    const langData = translations[currentLang];
    try {
        const res = await fetch(`${API_BASE}/delete`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: json = JSON.stringify({ type, name })
        });
        
        if (!res.ok) {
            const errData = await res.json();
            throw new Error(errData.error || "Failed to delete");
        }
        
        showToast(langData["toast-deleted"]);
        
        // Refresh everything
        loadNotes();
        loadGraph();
        loadManagementData();
        
        // If note viewer is displaying the deleted note, clear it
        if (type === "wiki") {
            noteContentArea.innerHTML = `
                <div class="note-content-area" id="note-content-area">
                    <div class="note-viewer-empty">
                        <i class="fa-solid fa-file-import empty-icon"></i>
                        <p data-i18n="note-empty">${langData["note-empty"]}</p>
                    </div>
                </div>
            `;
        }
    } catch (err) {
        showToast(langData["toast-delete-fail"] + err.message, true);
    }
}

async function runWebClipper() {
    const url = clipperUrlInput.value.trim();
    if (!url) return;
    
    const langData = translations[currentLang];
    try {
        btnClip.disabled = true;
        btnClip.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> ...`;
        showToast(langData["toast-clipping"]);
        
        const res = await fetch(`${API_BASE}/clip`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url })
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Failed to clip");
        
        showToast(langData["toast-clip-success"] + data.message);
        clipperUrlInput.value = "";
        
        // Refresh raw list in management tab if loaded
        if (document.getElementById("manage-tab").classList.contains("active")) {
            loadManagementData();
        }
    } catch (err) {
        showToast(langData["toast-clip-fail"] + err.message, true);
    } finally {
        btnClip.disabled = false;
        btnClip.innerHTML = `<i class="fa-solid fa-scissors"></i> <span data-i18n="action-clip">${langData["action-clip"]}</span>`;
    }
}

// 11. Git status checking & commit
async function checkGitStatus() {
    const langData = translations[currentLang];
    try {
        const res = await fetch(`${API_BASE}/git-status`);
        if (!res.ok) throw new Error("Failed to check Git status");
        const data = await res.json();
        
        if (data.is_clean) {
            gitStatusBadge.innerText = langData["git-status-clean"];
            gitStatusBadge.className = "git-badge badge-clean";
            gitControls.style.display = "none";
        } else {
            gitStatusBadge.innerText = langData["git-status-dirty"];
            gitStatusBadge.className = "git-badge badge-dirty";
            gitControls.style.display = "block";
        }
    } catch (err) {
        console.error(err);
    }
}

async function commitGitChanges() {
    const langData = translations[currentLang];
    const message = gitCommitMsgInput.value.trim();
    if (!message) {
        showToast("Commit message is required", true);
        return;
    }
    
    try {
        btnGitCommit.disabled = true;
        showToast(langData["toast-git-committing"]);
        
        const res = await fetch(`${API_BASE}/git-commit`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Failed to commit");
        
        showToast(langData["toast-git-committed"]);
        gitCommitMsgInput.value = "";
        checkGitStatus();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnGitCommit.disabled = false;
    }
}

// 12. Garbage collection of unreferenced raw sources
async function cleanupRawSources() {
    const langData = translations[currentLang];
    try {
        btnCleanupRaw.disabled = true;
        const res = await fetch(`${API_BASE}/cleanup-raw`, { method: "POST" });
        const data = await res.json();
        
        if (!res.ok) throw new Error(data.error || "Cleanup failed");
        
        const freedKb = (data.space_freed_bytes / 1024).toFixed(1);
        showToast(langData["toast-cleanup-raw-success"] + `${data.deleted_count} files (${freedKb} KB)`);
        
        // Refresh raw files view in management tab
        loadManagementData();
        checkGitStatus(); // Changes to raw files might trigger git modifications
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnCleanupRaw.disabled = false;
    }
}

// 13. Deep-linking to local Obsidian app
function copyObsidianLink() {
    const langData = translations[currentLang];
    const fileName = btnCopyObsidian.getAttribute("data-file");
    if (!fileName) return;
    
    const vaultName = "Wiki";
    const filePath = `wiki/${fileName}`;
    const obsidianUri = `obsidian://open?vault=${encodeURIComponent(vaultName)}&file=${encodeURIComponent(filePath)}`;
    
    navigator.clipboard.writeText(obsidianUri).then(() => {
        showToast(langData["toast-copy-obsidian"]);
    }).catch(err => {
        showToast("Failed to copy link: " + err, true);
    });
}

// 14. Graph Filter Legend
function initGraphFilters() {
    const select = document.getElementById("graph-filter-select");
    if (!select) return;
    select.addEventListener("change", (e) => {
        const filterType = e.target.value;
        // Reset all to false first if not "all"
        if (filterType !== "all") {
            Object.keys(activeGraphFilters).forEach(k => activeGraphFilters[k] = false);
            activeGraphFilters[filterType] = true;
        } else {
            Object.keys(activeGraphFilters).forEach(k => activeGraphFilters[k] = true);
        }
        filterGraph();
    });
}

function filterGraph() {
    if (!network || !rawGraphData) return;
    
    const colors = {
        overview: { background: "#78350f", border: "#f59e0b", highlight: { background: "#fbbf24", border: "#f59e0b" } },
        summary: { background: "#064e3b", border: "#10b981", highlight: { background: "#34d399", border: "#10b981" } },
        concept: { background: "#0c4a6e", border: "#06b6d4", highlight: { background: "#67e8f9", border: "#06b6d4" } },
        entity: { background: "#4c1d95", border: "#8b5cf6", highlight: { background: "#c084fc", border: "#8b5cf6" } },
        system: { background: "#1e293b", border: "#475569", highlight: { background: "#64748b", border: "#475569" } }
    };
    
    const filteredNodes = rawGraphData.nodes.filter(node => {
        const group = node.group || "concept";
        return activeGraphFilters[group] !== false;
    });
    
    const nodes = filteredNodes.map(node => {
        const c = colors[node.group] || colors.concept;
        return {
            id: node.id,
            label: node.label,
            color: {
                background: c.background,
                border: c.border,
                highlight: c.highlight
            },
            font: { color: "#f8fafc", face: "Plus Jakarta Sans", size: 11 },
            shape: node.group === "system" ? "box" : "dot",
            size: node.group === "overview" ? 12 : 6,
            borderWidth: 2
        };
    });
    
    network.setData({
        nodes: new vis.DataSet(nodes),
        edges: new vis.DataSet(rawGraphData.edges)
    });
}

// 15. Load and render Recent Updates
async function loadRecentUpdates() {
    try {
        const res = await fetch(`${API_BASE}/recent`);
        if (!res.ok) throw new Error("Failed to load recent updates");
        const data = await res.json();
        
        if (data.length === 0) {
            recentUpdatesList.innerHTML = `<li style="font-size: 10px; color: var(--text-muted); text-align: center; padding: 10px 0;">No updates yet</li>`;
            return;
        }
        
        recentUpdatesList.innerHTML = data.map(item => `
            <li class="recent-item" onclick="loadNoteDetail('${item.name}')">
                <div class="recent-item-title">${item.title}</div>
                <div class="recent-item-meta">
                    <span class="note-type-badge type-${item.type}" style="font-size: 8px; padding: 1px 4px;">${item.type}</span>
                    <span>${item.timestamp}</span>
                </div>
            </li>
        `).join("");
    } catch (err) {
        console.error(err);
    }
}

// 16. Load and render Drafts Review Queue
async function loadDrafts() {
    try {
        const res = await fetch(`${API_BASE}/drafts`);
        if (!res.ok) throw new Error("Failed to load drafts list");
        activeDrafts = await res.json();
        
        // Update tab badge count
        if (activeDrafts.length > 0) {
            draftsCountBadge.innerText = activeDrafts.length;
            draftsCountBadge.style.display = "inline-block";
        } else {
            draftsCountBadge.style.display = "none";
        }
        
        renderDraftsList(activeDrafts);
    } catch (err) {
        showToast(err.message, true);
    }
}

function renderDraftsList(drafts) {
    if (drafts.length === 0) {
        draftsListEl.innerHTML = `<div style="font-size: 11px; color: var(--text-muted); text-align: center; padding: 20px 0;">Queue is empty</div>`;
        draftEditorContent.style.display = "none";
        draftEditorEmpty.style.display = "flex";
        currentDraftName = null;
        return;
    }

    draftsListEl.innerHTML = drafts.map(draft => {
        const isActive = draft.name === currentDraftName ? "active" : "";
        return `
        <div class="draft-item-row ${isActive}" data-name="${draft.name}">
            <input type="checkbox" data-cb-draft onchange="updateDraftsBulkBar()" onclick="event.stopPropagation()">
            <span class="draft-item-name"><i class="fa-solid fa-file-pen" style="color:var(--primary);font-size:10px;"></i> ${draft.title || draft.name}</span>
        </div>`;
    }).join("");

    draftsListEl.querySelectorAll(".draft-item-row").forEach(item => {
        item.addEventListener("click", (e) => {
            if (e.target.type === "checkbox") return;
            loadDraftDetail(item.dataset.name);
        });
    });

    const saAll = document.getElementById("drafts-select-all");
    if (saAll) saAll.onchange = () => {
        draftsListEl.querySelectorAll("input[data-cb-draft]").forEach(cb => cb.checked = saAll.checked);
        updateDraftsBulkBar();
    };
    updateDraftsBulkBar();
}

async function loadDraftDetail(name) {
    try {
        currentDraftName = name;
        draftsListEl.querySelectorAll(".draft-item").forEach(item => {
            if (item.getAttribute("data-name") === name) {
                item.classList.add("active");
            } else {
                item.classList.remove("active");
            }
        });
        
        draftEditorEmpty.style.display = "none";
        draftEditorContent.style.display = "flex";
        draftEditorTextarea.value = "Loading draft content...";
        
        const res = await fetch(`${API_BASE}/draft-detail?name=${encodeURIComponent(name)}`);
        if (!res.ok) throw new Error("Failed to load draft detail");
        const data = await res.json();
        
        draftReviewTitle.innerText = `Reviewing: ${data.name}`;
        draftEditorTextarea.value = data.content;
    } catch (err) {
        showToast(err.message, true);
    }
}

async function approveCurrentDraft() {
    if (!currentDraftName) return;
    const langData = translations[currentLang];
    
    try {
        btnApproveDraft.disabled = true;
        btnApproveDraft.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Processing...`;
        
        const res = await fetch(`${API_BASE}/approve-draft`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: currentDraftName,
                content: draftEditorTextarea.value
            })
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Approval failed");
        
        showToast(langData["toast-draft-approved"]);
        currentDraftName = null;
        
        loadDrafts();
        loadNotes();
        loadGraph();
        loadRecentUpdates();
        checkGitStatus();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnApproveDraft.disabled = false;
        btnApproveDraft.innerHTML = `<i class="fa-solid fa-check"></i> <span data-i18n="btn-approve">${langData["btn-approve"]}</span>`;
    }
}

async function rejectCurrentDraft() {
    if (!currentDraftName) return;
    const langData = translations[currentLang];
    
    if (!confirm(langData["confirm-delete"])) return;
    
    try {
        btnRejectDraft.disabled = true;
        
        const res = await fetch(`${API_BASE}/reject-draft`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: currentDraftName })
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Rejection failed");
        
        showToast(langData["toast-draft-rejected"]);
        currentDraftName = null;
        loadDrafts();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnRejectDraft.disabled = false;
    }
}

// 17. Top search live matching dropdown
let topSearchTimeout = null;
function handleTopSearchInput(e) {
    clearTimeout(topSearchTimeout);
    const query = topSearchInput.value.trim();
    
    if (!query) {
        topSearchResults.style.display = "none";
        return;
    }
    
    topSearchTimeout = setTimeout(() => {
        runTopSearch(query);
    }, 250);
}

async function runTopSearch(query) {
    try {
        const res = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        if (!res.ok) throw new Error("Search failed");
        
        const matches = notesData.filter(note => 
            note.title.toLowerCase().includes(query.toLowerCase()) || 
            note.description.toLowerCase().includes(query.toLowerCase())
        ).slice(0, 8);
        
        renderTopSearchResults(matches);
    } catch (err) {
        console.error(err);
    }
}

function renderTopSearchResults(results) {
    if (results.length === 0) {
        topSearchResults.innerHTML = `<div style="padding: 10px 16px; font-size: 12px; color: var(--text-muted); text-align: center;">No matches found</div>`;
        topSearchResults.style.display = "block";
        return;
    }
    
    topSearchResults.innerHTML = results.map(item => `
        <div class="search-dropdown-item" onclick="selectTopSearchResult('${item.name}')">
            <span class="search-dropdown-title"><i class="fa-solid fa-file-invoice"></i> ${item.title}</span>
            <span class="note-type-badge type-${item.type}" style="font-size: 8px; padding: 1px 4px;">${item.type}</span>
        </div>
    `).join("");
    topSearchResults.style.display = "block";
}

function selectTopSearchResult(name) {
    topSearchInput.value = "";
    topSearchResults.style.display = "none";
    loadNoteDetail(name);
}

// Bind to window to prevent event scope errors
window.selectTopSearchResult = selectTopSearchResult;
window.loadNoteDetail = loadNoteDetail;

async function approveAllDrafts() {
    const langData = translations[currentLang];
    if (activeDrafts.length === 0) return;
    
    if (!confirm(langData["confirm-delete"])) return;
    
    try {
        btnApproveAll.disabled = true;
        btnApproveAll.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i>`;
        showToast(langData["toast-git-committing"] || "Processing...");
        
        const res = await fetch(`${API_BASE}/approve-all`, {
            method: "POST"
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Batch approval failed");
        
        showToast(langData["toast-drafts-approved-all"]);
        currentDraftName = null;
        
        loadDrafts();
        loadNotes();
        loadGraph();
        loadRecentUpdates();
        checkGitStatus();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnApproveAll.disabled = false;
        btnApproveAll.innerHTML = `<i class="fa-solid fa-check-double"></i> <span data-i18n="btn-approve-all">${langData["btn-approve-all"]}</span>`;
    }
}

async function rejectAllDrafts() {
    const langData = translations[currentLang];
    if (activeDrafts.length === 0) return;
    
    if (!confirm(langData["confirm-delete"])) return;
    
    try {
        btnRejectAll.disabled = true;
        btnRejectAll.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i>`;
        
        const res = await fetch(`${API_BASE}/reject-all`, {
            method: "POST"
        });
        
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Batch rejection failed");
        
        showToast(langData["toast-drafts-rejected-all"]);
        currentDraftName = null;
        loadDrafts();
    } catch (err) {
        showToast(err.message, true);
    } finally {
        btnRejectAll.disabled = false;
        btnRejectAll.innerHTML = `<i class="fa-solid fa-trash-can"></i> <span data-i18n="btn-reject-all">${langData["btn-reject-all"]}</span>`;
    }
}

// ═══════════════════════════════════════════
// BULK SELECT BAR HELPERS
// ═══════════════════════════════════════════

function updateWikiBulkBar() {
    const checked = [...manageWikiListEl.querySelectorAll("input[data-cb-wiki]:checked")];
    const btn = document.getElementById("btn-wiki-delete-selected");
    const counter = document.getElementById("wiki-del-count");
    if (btn) { btn.style.display = checked.length > 0 ? "inline-flex" : "none"; }
    if (counter) counter.textContent = checked.length;
}

function updateRawBulkBar() {
    const checked = [...manageRawListEl.querySelectorAll("input[data-cb-raw]:checked")];
    const btn = document.getElementById("btn-raw-delete-selected");
    const counter = document.getElementById("raw-del-count");
    if (btn) { btn.style.display = checked.length > 0 ? "inline-flex" : "none"; }
    if (counter) counter.textContent = checked.length;
}

function updateDraftsBulkBar() {
    const checked = [...draftsListEl.querySelectorAll("input[data-cb-draft]:checked")];
    const btnApprove = document.getElementById("btn-approve-selected");
    const btnDelete = document.getElementById("btn-delete-selected-drafts");
    const cntA = document.getElementById("drafts-approve-count");
    const cntD = document.getElementById("drafts-del-count");
    const show = checked.length > 0 ? "inline-flex" : "none";
    if (btnApprove) btnApprove.style.display = show;
    if (btnDelete) btnDelete.style.display = show;
    if (cntA) cntA.textContent = checked.length;
    if (cntD) cntD.textContent = checked.length;
}

// Wire bulk delete buttons once DOM is ready (delayed bind after first render)
document.addEventListener("DOMContentLoaded", () => {
    const btnWikiDel = document.getElementById("btn-wiki-delete-selected");
    if (btnWikiDel) btnWikiDel.addEventListener("click", async () => {
        const names = [...manageWikiListEl.querySelectorAll("input[data-cb-wiki]:checked")]
            .map(cb => cb.closest("[data-name]")?.dataset.name).filter(Boolean);
        if (!names.length) return;
        if (!confirm(`Xóa ${names.length} file wiki đã chọn?`)) return;
        const res = await fetch(`${API_BASE}/delete-bulk`, {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filenames: names, type: "wiki" })
        });
        const data = await res.json();
        showToast(data.message || `Đã xóa ${names.length} file.`);
        loadManagementData();
    });

    const btnRawDel = document.getElementById("btn-raw-delete-selected");
    if (btnRawDel) btnRawDel.addEventListener("click", async () => {
        const names = [...manageRawListEl.querySelectorAll("input[data-cb-raw]:checked")]
            .map(cb => cb.closest("[data-name]")?.dataset.name).filter(Boolean);
        if (!names.length) return;
        if (!confirm(`Xóa ${names.length} file nguồn đã chọn?`)) return;
        const res = await fetch(`${API_BASE}/delete-bulk`, {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filenames: names, type: "raw" })
        });
        const data = await res.json();
        showToast(data.message || `Đã xóa ${names.length} file.`);
        loadManagementData();
    });

    const btnDraftApprove = document.getElementById("btn-approve-selected");
    if (btnDraftApprove) btnDraftApprove.addEventListener("click", async () => {
        const names = [...draftsListEl.querySelectorAll("input[data-cb-draft]:checked")]
            .map(cb => cb.closest("[data-name]")?.dataset.name).filter(Boolean);
        if (!names.length) return;
        const res = await fetch(`${API_BASE}/approve-bulk`, {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filenames: names })
        });
        const data = await res.json();
        showToast(data.message || `Đã duyệt ${names.length} bản thảo.`);
        loadDrafts();
    });

    const btnDraftDel = document.getElementById("btn-delete-selected-drafts");
    if (btnDraftDel) btnDraftDel.addEventListener("click", async () => {
        const names = [...draftsListEl.querySelectorAll("input[data-cb-draft]:checked")]
            .map(cb => cb.closest("[data-name]")?.dataset.name).filter(Boolean);
        if (!names.length) return;
        if (!confirm(`Xóa ${names.length} bản thảo đã chọn?`)) return;
        const res = await fetch(`${API_BASE}/delete-bulk`, {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filenames: names, type: "draft" })
        });
        const data = await res.json();
        showToast(data.message || `Đã xóa ${names.length} bản thảo.`);
        loadDrafts();
    });
});

window.updateWikiBulkBar = updateWikiBulkBar;
window.updateRawBulkBar = updateRawBulkBar;
window.updateDraftsBulkBar = updateDraftsBulkBar;
