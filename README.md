# Resume Toolkit — Prabhjot (Prabh) Singh

A personal resume management and job-search toolkit powered by Claude Code agent workflows. Maintains master resume templates, generates job-tailored versions, and produces Google dorks for targeted job hunting.

---

## Project Structure

```
resume/
├── resume.html                        # Master template — Version A (MidnightBlue, compact, two-column bottom)
├── resume-b.html                      # Master template — Version B (clean, dark-accented, linear)
├── resume-c.html                      # Version C — mirrors original PDF layout exactly
├── prabh_resume_pythonAWS.pdf         # Source PDF resume
├── .agent/workflows/
│   ├── tailor-made-resume.md          # Workflow: AI-tailors resume to a job description
│   └── generate-job-dorks.md          # Workflow: Generates Google search dorks for job hunting
├── versions/tailored/                 # Output dir (gitignored) — tailored resumes go here
└── README.md
```

---

## Resume Versions

| File | Style | ATS | Use Case |
|---|---|---|---|
| `resume-c.html` | Mirrors original PDF — justified, single-column | ✅ Best | Default for all applications |
| `resume-b.html` | Clean dark-accented, linear layout | ✅ Good | Modern tech companies, startup portals |
| `resume.html` | MidnightBlue headers, two-column bottom section | ⚠️ Weakest | Human reviewers only — two-column layout can scramble ATS text extraction |

All versions include a hidden ATS optimization block (invisible to readers, extractable by ATS text parsers) with full keyword coverage of your tech stack, achievements, and target roles.

---

## Converting HTML to PDF

### Recommended: `convert_to_pdf.py` (Playwright)

No headers/footers, hyperlinks preserved, margins controlled by `@page` CSS.

**One-time setup:**
```bash
pip3 install playwright
python3 -m playwright install chromium
```

**Convert:**
```bash
# Output filename matches input (resume-c.pdf)
python3 convert_to_pdf.py resume-c.html

# Or specify output name
python3 convert_to_pdf.py resume-c.html my-resume.pdf
```

### Alternative: Browser Print Dialog (easiest to verify visually)

1. Open the HTML file in Chrome
2. `Ctrl+P`
3. Set **Destination** → Save as PDF
4. **More settings** → uncheck **Headers and footers**
5. Set **Margins** → None (the `@page` CSS handles margins)
6. Save

### Why not Chrome CLI directly

`google-chrome --headless=new --print-to-pdf-no-header` is unreliable on Chrome 112+ — the flag does not consistently suppress the date/title/page-number header and footer. The Playwright script explicitly sets `display_header_footer=False` via the DevTools Protocol, which works reliably.

| Tool | Hyperlinks | CSS Flexbox | No Headers/Footers | Verdict |
|---|---|---|---|---|
| `convert_to_pdf.py` (Playwright) | ✅ | ✅ | ✅ | **Use this** |
| Browser Ctrl+P | ✅ | ✅ | ✅ (manual toggle) | Good for visual check |
| Chrome CLI `--headless` | ✅ | ✅ | ❌ unreliable | Avoid |
| wkhtmltopdf | ✅ | ❌ old WebKit | ✅ | Breaks layout |
| WeasyPrint | ⚠️ | ⚠️ | ✅ | Not recommended |

---

## Agent Workflows

These `.agent/workflows/` files run as slash commands inside Claude Code. No build system or server needed.

### Workflow 1: Tailor Resume to a Job Description

Optimizes a resume for a specific job posting — reorders skills and bullets by relevance, rewrites the summary to mirror JD language, updates ATS keywords, and sets the HTML `<title>` to the company name. Never fabricates experience, dates, or companies.

**What gets optimized:**
- Professional summary (mirrored to JD language)
- Technical skills (reordered by JD relevance)
- Experience bullet points (reordered best-to-least relevant)
- Hidden ATS block (fully rewritten for the role)
- HTML `<title>` tag (set to candidate name + company)

**Usage — paste this into Claude Code:**
```
Tailor my resume for this job: [paste full JD here], save as resume-[company]-[role]
```

**Output:** `versions/tailored/{resume_name}.html`
Add `"both versions"` to your prompt to also generate a `-b` variant.

---

### Workflow 2: Generate Cover Letter

Reads `resume-c.html` and the job description, then generates a concise plain-text cover letter under 100 words — no filler, no fabrication, only content traceable to your actual resume.

**Rules:**
- Strictly under 100 words
- Plain text, single paragraph — no headers, no bullets
- Only uses content from `resume-c.html` — never invents experience or metrics
- Mirrors key JD terminology naturally

**Usage — paste this into Claude Code:**
```
Generate a cover letter for this job: [paste full JD here], save as coverletter-[company]-[role]
```

**Output:** `versions/cover_letter/{file_name}.txt` (gitignored)

---

### Workflow 3: Generate Google Dorks for Job Hunting

Reads your resume, extracts your tech stack, seniority, and role keywords, then generates optimized Google search queries targeting specific ATS platforms and job boards.

**Covered ATS platforms:** Greenhouse, Lever, Ashby, Workday, SmartRecruiters, BambooHR, iCIMS, Jobvite, Teamtailor, Personio, Comeet, Recruitee

**Covered job boards:** Wellfound, RemoteOK, WeWorkRemotely, Remotive, Working Nomads, Jobspresso, Authentic Jobs, FlexJobs, Arc, Indeed, LinkedIn Jobs

**Usage — paste this into Claude Code:**
```
Generate job dorks for [contractor/freelance/full-time] roles in [US/Canada/Europe/LATAM]
```

**Output:** Copy-ready Google dork queries grouped by platform, formatted in markdown code blocks.

---

## How the Hidden ATS Block Works

Each resume contains a `div` with `class="hidden-ast"` (deliberately reversed from "ATS" to avoid pattern detection). It is hidden from visual readers via CSS:

```css
position: absolute;
left: -9999px;    /* pushed off-screen */
font-size: 1px;
opacity: 0.01;
```

When Chrome converts the HTML to PDF, it renders the page first — the div is off-screen and invisible. However, Chrome still embeds all rendered text into the PDF's text layer. ATS systems typically extract raw text from the PDF (they don't render it visually), so they pick up the keyword-rich content in that hidden block.

> This is a grey-area technique. It works on many ATS platforms but sophisticated systems may detect and filter hidden/invisible text. The primary ATS optimization is always the visible content.

---

## Tailoring Rules (enforced by workflow)

| Allowed | Forbidden |
|---|---|
| Reorder skills by relevance | Fabricate experience, dates, or companies |
| Reorder bullet points | Add skills the candidate doesn't have |
| Adjust wording to match JD terminology | Change HTML structure or CSS |
| Rewrite professional summary | Modify contact information |
| Rewrite hidden ATS block | Change company names or dates |
| Update HTML `<title>` with company name | |
