---
name: opportunities-newsletter
description: Drafts Sam Fox's "Opportunities Newsletter" student newsletter — a roundup of currently-open internships, fellowships, conferences, student programs, online courses, and essay competitions at classical liberal, libertarian, conservative, centre-right, and free-market think tanks globally. Each newsletter includes a filterable spreadsheet attachment. Trigger whenever Sam asks to write, draft, build, update, or refresh an "Opportunities Newsletter" edition; asks for an opportunities roundup or student program list; asks what's open for free-market students; or asks to check which programs from a previous newsletter are still open. Use this skill any time Sam mentions the phrase "Opportunities Newsletter" or references the regular student-facing roundup, even casually.
---

# Opportunities Newsletter

A skill for drafting Sam Fox's recurring "Opportunities Newsletter" student newsletter and its accompanying filterable spreadsheet. The newsletter goes to students in the classical liberal, libertarian, conservative, and centre-right space and lists currently-open programs at aligned think tanks and educational foundations.

## Critical principles (do not skip)

1. **Verify everything is genuinely open before listing it.** Past errors have included listing programs that closed weeks earlier, programs that hadn't yet opened, and programs with stale deadlines. This is the single most important quality bar.
2. **Direct URL fetching beats general search.** Going to a program's specific page returns more reliable deadline information than a search engine query.
3. **Re-verify close to send date.** Some organisation pages (especially Vinson Centre, freedomweek.org, IEA programme pages) update frequently. A deadline confirmed three weeks ago may have shifted.
4. **When uncertain, be honest in the copy.** Use "Apply early," "Rolling," "Contact for current application window," or "Applications open" rather than guessing a specific deadline. Never invent a deadline.
5. **Drop anything you cannot verify as open** by the planned send date — better a shorter, accurate newsletter than a long one with broken or closed listings.
6. **Closed programs are not included** — neither in the email body nor in the spreadsheet. The spreadsheet is a live, currently-open snapshot only.
7. **Allow repeats while programs are still open.** Search Sam's Gmail for prior threads first for context, but do not suppress a program merely because it appeared in a previous newsletter. Re-list it for however many newsletters are useful if applications are still open, the deadline is still ahead, or the opportunity remains relevant to readers.
8. **Do not use the word "genuinely."** Sam has flagged it as overused.

## Workflow

### Step 1: Find what's been covered before

Use the Gmail search tool with: `subject:"Opportunities Newsletter"` (no exclamation mark). Pull the most recent thread or two with `messageFormat: FULL_CONTENT` to see which programs were featured. Programs from previous newsletters can and should be re-featured for however many newsletters are needed if deadlines are still ahead, applications are still open, or the opportunity remains useful to readers. Do not suppress a program merely because it appeared in an earlier newsletter.

### Step 2: Build the candidate list

Read `references/organisations.md` for the full tiered list of target organisations. The list is structured as:

- **Tier 1** — check every newsletter (highest-yield programs with regular cycles or rolling intakes)
- **Tier 2** — check every 2–3 newsletters (active orgs but lower-frequency programs)
- **Tier 3** — Atlas Network directory as master source for orgs not individually listed

For each candidate program, capture:
- Organisation name
- Program name
- Application status (open / closed / not yet open) — only "open" entries make it into the newsletter and spreadsheet
- Specific deadline if visible on the live page (otherwise: rolling, apply early, or "contact for window")
- Type (Internship, Conference, Fellowship, Essay competition, Online course, Seminar, Scholarship, or Other)
- Duration
- Paid? (Yes — amount; No; Stipend only)
- International eligibility (Yes / No / Some restrictions)
- A one-paragraph description (3–5 sentences) covering what the program is, dates, cost/stipend, and how to apply
- Apply URL

### Step 3: Verify everything

Cross-check each program one more time. Read `references/known-traps.md` before finalising — it lists programs that have specifically caused problems in past newsletters.

### Step 4: Draft the newsletter email

Read `references/template.md` for the exact email format. Subject is `Opportunities Newsletter`. The country order is fixed: 🇦🇺 Australia → 🇳🇿 New Zealand → 🇬🇧 United Kingdom → 🇪🇺 Europe (if any) → 🇺🇸 United States → 🇨🇦 Canada → 🌏 Asia / Latin America / MENA / Africa (only if relevant programs are open) → 🌐 Online courses. Skip any country with no currently-open programs.

### Step 5: Generate the spreadsheet

Read `references/spreadsheet-schema.md` for the exact column structure and allowed values. Generate the spreadsheet using the xlsx skill — see `/mnt/skills/public/xlsx/SKILL.md` for skill mechanics. Save the file as `opportunities-newsletter-YYYY-MM-DD.xlsx` in `/mnt/user-data/outputs/` and ensure it includes only currently-open programs.

### Step 6: Output

1. Use the message composition tool with `kind: email` and `subject: "Opportunities Newsletter"` to deliver the email body.
2. Use `present_files` to share the spreadsheet attachment.
3. Give Sam a short summary of:
   - What was kept from the previous newsletter
   - What was dropped (and why — e.g. "deadline passed", "not yet open")
   - What was newly added
   - Any items you couldn't fully verify and what assumption was made

## Tone & style

- Direct, warm, and confident — Sam writes like he's talking to fellow students, not pitching corporate.
- Each program in the email gets a single paragraph (3–5 sentences). Don't pad. Don't use marketing puffery.
- Use specific deadlines where verified; honest hedges where not.
- Country header format: `🇦🇺 AUSTRALIA` (flag emoji, space, all caps, on its own line, no markdown).
- Program header format: `Organisation Name — Program Name | Deadline or Status`
- URLs go on their own line after the description paragraph, no markdown link syntax.
- Sign off as "Best, Sam" — do NOT include a full signature block. Gmail auto-appends Sam's signature.

## When to ask Sam vs. just proceed

- **Just proceed**: when checking org pages, verifying deadlines, building the country/category structure, drafting the email body, generating the spreadsheet.
- **Ask Sam**: if a major new organisation should be added that isn't in `references/organisations.md`, if the date range covered should expand (e.g. include programs opening in 2–3 months), or if Sam has specific contacts at programs that should be name-checked.

## File map

- `references/organisations.md` — tiered list of target organisations grouped by country and region
- `references/template.md` — exact email template with intro, opt-out line, signup link, sign-off, and spreadsheet attachment footer
- `references/spreadsheet-schema.md` — column structure and allowed values for the filterable Excel attachment
- `references/known-traps.md` — programs that have caused verification errors in past newsletters
