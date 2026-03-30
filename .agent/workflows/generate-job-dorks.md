---
description: Generate Google Job Search Dorks based on User's Resume
---

You are an expert in Google dorking for job search.

## GOAL
Generate advanced Google search dorks to find remote software developer roles based on the user's resume, specific contract types, and regions.

## INPUT VARIABLES
- `contract_type`: The desired contract type (e.g., contractor, freelance, 1099, B2B)
- `regions`: Target regions or locations (e.g., US, Europe, LATAM)

## REQUIRED FILES TO READ
- `resume-c.html` (default master resume — or any other specified resume file)

## WORKFLOW

### Step 1: Analyze the Resume
Read the user's resume file and extract the following information automatically:
- **Tech Stack**: Identify the primary programming languages, frameworks, and tools the user is proficient in.
- **Seniority**: Determine the user's seniority level based on their years of experience and job titles (e.g., Senior, Lead).
- **Role Keywords**: Extract key job titles and domain-specific roles the user targets (e.g., Backend Engineer, Full Stack, AI).

### Step 2: Generate Google Dorks
Using the extracted `Tech Stack`, `Seniority`, and `Role Keywords`, along with the provided `contract_type` and `regions`, generate optimized Google dorks.

1. Generate optimized Google dorks for EACH of the following ATS platforms:
   - Greenhouse (boards.greenhouse.io)
   - Lever (jobs.lever.co)
   - Ashby (jobs.ashbyhq.com)
   - Workday (myworkdayjobs.com / wd1.myworkdayjobs.com)
   - SmartRecruiters (careers.smartrecruiters.com)
   - BambooHR (jobs.bamboohr.com)
   - iCIMS (careers.icims.com)
   - Jobvite (jobs.jobvite.com)
   - Teamtailor (career.teamtailor.com)
   - Personio (jobs.personio.de)
   - Comeet (jobs.comeet.co)
   - Recruitee (jobs.recruitee.com)

2. Generate optimized Google dorks for these job boards:
   - Wellfound (wellfound.com)
   - RemoteOK (remoteok.com)
   - WeWorkRemotely (weworkremotely.com)
   - Remotive (remotive.com)
   - Working Nomads (workingnomads.com)
   - Jobspresso (jobspresso.co)
   - Authentic Jobs (authenticjobs.com)
   - FlexJobs (flexjobs.com)
   - Arc (arc.dev)
   - Indeed (indeed.com)
   - LinkedIn Jobs (linkedin.com/jobs)

### Step 3: Dork Requirements
Each dork must:
- Include "remote" and the locations defined in `regions`.
- Include contract-related terms defined in `contract_type` (e.g., contract, contractor, freelance, 1099).
- Include the extracted `Tech Stack` and `Role Keywords`.
- Exclude internships and junior roles unless the extracted `Seniority` explicitly suggests otherwise.
- Be optimized for Google search (use OR, parentheses, intitle:, inurl:, site:, etc.).

### Step 4: Output Format
- Group by ATS platforms.
- Group by Job Boards.
- Provide at least 2 strong variations per platform.
- Use clean markdown code block formatting for the generated dorks so they can be easily copied.
- Do not explain anything — only output the dorks.

IMPORTANT: Observe high signal, low noise. Use boolean operators properly. Avoid generic searches.
