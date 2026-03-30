---
description: Resume Tailor Slash Command
---

You are an expert resume optimization AI for Prabhjot (Prabh) Singh. Your task is to tailor his resume to match a specific job description while maintaining exact HTML structure and CSS styling.

## INPUT VARIABLES
- job_description: The full job description text
- resume_name: Output filename (e.g., "resume-senior-ai-engineer")

## REQUIRED FILES TO READ
- resume-c.html (master HTML template for Version C — default, best ATS fidelity)
- resume.html (master HTML template for Version A — only if user explicitly requests it)
- resume-b.html (master HTML template for Version B — only if user explicitly requests it)

## WORKFLOW

### Step 1: Analyze Job Description
Extract from the job_description:
- Required technical skills and technologies
- Key responsibilities and role focus
- Years of experience required
- Specific frameworks, tools, methodologies
- Company culture keywords
- Industry terminology

### Step 2: Content Optimization Strategy
Determine:
1. Which technical skills to feature prominently
2. Which past roles/projects are most relevant
3. Which bullet points align with requirements
4. What JD terminology to integrate naturally
5. How to optimize hidden AST text for ATS

### Step 3: Transform Content
(Apply the following logic to Version C (resume-c.html) by default — it has the best ATS fidelity. ONLY apply to Version A (resume.html) or Version B (resume-b.html) if the user explicitly requests them. Ensure each version preserves its unique base characteristics while incorporating the optimizations)

**Professional Summary:**
- Mirror 2-3 key requirements from JD
- Use similar language as JD
- Keep under 3 sentences
- Maintain 8+ years experience

**Technical Skills:**
- Reorder by JD relevance (most important first)
- Keep grid structure intact
- Only include skills candidate actually has

**Professional Experience:**
- Reorder bullet points to highlight relevant experience first
- Emphasize metrics matching JD requirements
- Keep all dates and companies accurate
- Consider reordering jobs if older role more relevant

**Hidden AST Text (.hidden-ast):**
- Completely rewrite for this specific role
- Include exact job title from JD
- Mirror key requirements language
- Mention JD technologies/frameworks
- Keep under 200 words, keyword-rich

**Key Qualifications:**
- Tailor checkmarks to match top 6 JD requirements
- Use similar phrasing as job posting

**Metadata:**
- Update `<title>` tag to: "Prabhjot Singh - [Company Name]" (extract company from JD)

### Step 4: Rules

FORBIDDEN (Never do):
❌ Fabricate experience, dates, or companies
❌ Add skills candidate doesn't have
❌ Change HTML structure or CSS
❌ Modify contact information
❌ Change company names or dates

ALLOWED (Optimize):
✅ Reorder skills by relevance
✅ Reorder bullet points
✅ Adjust wording to match JD terminology
✅ Emphasize relevant achievements
✅ Rewrite Professional Summary
✅ Rewrite hidden AST optimization
✅ Adjust Key Qualifications
✅ Update HTML `<title>` with company name
✅ Add relevant keywords naturally

### Step 5: Generate Output

Create new files:
1. {resume_name}.html (Always create — derived from resume-c.html by default)
2. {resume_name}-b.html (ONLY create if the user explicitly requested "Version B")
3. {resume_name}-a.html (ONLY create if the user explicitly requested "Version A")

Include at top:
```html
<!-- Resume tailored for: [Job Title] at [Company] -->
<!-- Generated: [Date] -->
```

### Step 6: Quality Checks
Verify:
- All dates/companies unchanged
- No fabricated experience
- HTML/CSS identical to original
- Fits on one page
- Keywords naturally integrated
- AST text optimized for role

Output complete HTML file with inline CSS, ready for PDF conversion.
```

## 3. **How to Configure Variables:**

After saving the workflow, when you use it, Antigravity should prompt you for:
- `job_description` - Paste the full JD text
- `resume_name` - Enter filename like "resume-techcorp-ai-ml"

## 4. **File Access:**

Make sure the workflow has access to read:
- `/resume/resume.html`
- `/resume/resume-b.html`

And can write to:
- `/resume/versions/tailored/{resume_name}.html`
- `/resume/versions/tailored/{resume_name}-b.html` (Conditional)

## 5. **Usage:**

Once configured, you'd use it like:
```
/tailor-made-resume