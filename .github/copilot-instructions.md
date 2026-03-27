# Quick Do PDF - AI Agent Instructions

Quick Do PDF is a **privacy-first, offline-capable PDF toolkit** with both client-side and server-side components. The project combines a static frontend site with a FastAPI backend for operations requiring server processing.

## Architecture Overview

### Frontend (Client-Side First)
- **Single HTML pages per tool** (e.g., `merge.html`, `compress.html`, `split.html`) using **pdf-lib** v1.17.1
- All client-side operations execute in the browser; files never leave the user's device
- Shared styling via `tools.css` with **CSS variable-based theming system** (theme-red, theme-blue, theme-green, etc.)
- **theme.js** manages light/dark mode via localStorage persistence
- Each page includes SEO content section (h2/h3 headers, FAQ blocks in `.tool-seo-content`)

### Backend (FastAPI Server)
- Located in `/backend/main.py` with dependencies in `requirements.txt`
- Handles **complex conversions** requiring server resources:
  - `POST /api/convert/pdf-to-word` uses `pdf2docx` library
  - `POST /api/convert/pdf-to-excel` uses `pdfplumber` + `pandas` for table extraction
  - Pike PDF operations for encryption/decryption
- **Session-based temp file management** with automatic cleanup via BackgroundTasks
- CORS enabled globally (`allow_origins=["*"]`)

### Site Structure
- `/blog/` - Long-form HTML articles with embedded SEO content (~800+ words)
- `index.html` - Landing page catalog of all tools
- Multiple Python scripts for **content automation** (blog generation, ad injection, SEO updates)

## Key Development Patterns

### Adding a New Tool Page
1. **Create new HTML file** copying structure from existing tool (e.g., `compress.html`)
2. **Set theme class** on body: `<body class="theme-[red|blue|green|gold|purple|amber]">`
3. **Include required scripts**:
   ```html
   <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
   <script src="theme.js"></script>
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3543763798528021"></script>
   ```
4. **Structure**: Upload zone → File processing logic → Success message
5. **Progress UI**: Use `updateProgress(percent, text)` pattern with progress bar updates
6. **Add SEO content** in `<section class="tool-seo-content">` at bottom with h2/h3/FAQ blocks

### CSS & Theming
- All colors use CSS custom properties (e.g., `var(--a1)`, `var(--bg)`, `var(--text)`)
- Theme-specific accent colors defined in `tools.css` root and `body.theme-*` selectors
- Responsive grid via `.option-grid` with `.cols2` or `.cols3` classes
- Reusable components: `.upload-zone`, `.action-btn`, `.option-card`, `.compare-card`

### JavaScript Patterns (Client-Side)
- **PDF Operations**: Access `PDFLib.PDFDocument` globally after script loads
- **File Handling**: Use drag-drop listeners on `#dropArea` with DataTransfer fallback
  ```javascript
  drop.addEventListener('drop', e => {
    e.preventDefault();
    const dt = new DataTransfer();
    [...e.dataTransfer.files].filter(f => f.type === 'application/pdf').forEach(f => dt.items.add(f));
    inp.files = dt.files;
  });
  ```
- **Blob Download Pattern**: Create anchor, set href to `URL.createObjectURL(blob)`, trigger click
- **Loader Control**: Add/remove `active` class on `#loader` div to show/hide spinner

### Backend Conversion Endpoints
- **Pattern**: Receive file via multipart form → Save to temp dir with UUID → Process → Return FileResponse
- **Cleanup Strategy**: Use `background_tasks.add_task(cleanup_files, path1, path2)` so downloads complete before deletion
- **Error Handling**: Raise `HTTPException(status_code=500, detail=str(e))` for user feedback
- **File Paths**: Always use `os.path.join(tempfile.gettempdir(), f"temp_{session_id}.ext")`

### Blog & Content Automation
- Blog articles in `/blog/` follow pattern: `<h2>`, `<h3>`, `<p>`, `<div class='seo-content-expansion'>`
- Generation scripts (`generate_new_blogs.py`) accept templates with placeholder strings
- Ad injection (`inject_adsense.py`) scans for `class="tool-seo-content"` and injects ads
- SEO updates via `update_seo.ps1` PowerShell script for title tag optimization

## Development Workflows

### Testing Client-Side Changes
1. Open tool HTML directly in browser (no build step needed)
2. Browser DevTools → Network tab to monitor PDF transformations
3. Test with various PDFs in `/tesseract-test/` folder if needed

### Testing Backend Changes
1. Ensure Python dependencies installed: `pip install -r backend/requirements.txt`
2. Start FastAPI: `uvicorn backend.main:app --reload`
3. Test endpoints via Postman (see `postman.json`) or curl

### Running Content Generators
- Blog generation: `python generate_new_blogs.py` → outputs new HTML files to `/blog/`
- Ad injection: `python inject_adsense.py` → modifies tool pages with ad blocks
- Sitemap: `python generate_sitemap.py` → updates `sitemap.xml`

## Important Constraints & Conventions

- **No external CDN dependencies** except: pdf-lib, PDF.js, jsPDF, Google Fonts, AdSense
- **File uploads are private**: Never transmit raw file bytes to external APIs except FastAPI backend
- **Progress indication required**: Always show `updateProgress()` for operations >1 second
- **Filename preservation**: Downloaded files should maintain original name minus extension (e.g., `document.pdf` → `document_merged.pdf`)
- **Response format**: PDF tools use consistent success message → auto-download pattern
- **Accessibility**: All buttons must have aria-labels; theme toggle icon must update dynamically

## Common File References

- **Shared styles**: [tools.css](tools.css) - CSS variables, component classes
- **Theme logic**: [theme.js](theme.js) - Dark/light mode, localStorage
- **Tool exemplars**: 
  - Client-only: [merge.html](merge.html) - Simple PDF merge with pdf-lib
  - Server operation: [backend/main.py](backend/main.py#L30-L45) - PDF to Word conversion pattern
- **Blog template**: [generate_new_blogs.py](generate_new_blogs.py#L1-L50) - Blog generation boilerplate
- **Index catalog**: [index.html](index.html) - Links to all tool pages

## Questions Before Implementation

When extending this codebase, ask yourself:
1. **Is this operation fast/simple enough for client-side?** → Use pdf-lib/PDF.js, keep file local
2. **Does it require heavy computation or external libs?** → Add endpoint to `/backend/main.py`
3. **Is this a new tool?** → Copy existing tool HTML, modify title/description/theme/logic
4. **Does content need to be search-discoverable?** → Add detailed SEO section with h2/h3/FAQ blocks
5. **Will this page get traffic?** → Include AdSense integration matching existing pages
