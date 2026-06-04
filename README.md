# Opportunities Newsletter Bot

A monthly automation that drafts Sam's "Opportunities Newsletter" student newsletter, saves it as a Gmail draft, and emails Sam to review. **Nothing is ever sent without Sam's review.**

## What it does

On the first Monday of every month (or whenever Sam triggers it manually), a GitHub Actions job runs `agent.py`. The script:

1. Asks Claude (acting as an agent) to read the skill files in `skill/`, search Sam's Gmail for recent "Opportunities Newsletter" editions, and verify every Tier-1/Tier-2 program in the skill's organisation list by fetching its application page.
2. Returns a structured payload describing only the **currently-open** programs.
3. Builds the email body (following `skill/references/template.md`) and a filterable `.xlsx` spreadsheet (following `skill/references/spreadsheet-schema.md`).
4. Saves the email as a **Gmail draft** in Sam's account with the spreadsheet attached.
5. Sends Sam a short notification email with a link to the draft.

Sam opens the draft, reviews/edits, and hits send when ready.

## What it does NOT do

- Send the newsletter directly. Drafts only.
- Add or remove programs from the canonical organisation list. That's a manual edit to `skill/references/organisations.md`.
- Promote a program from Tier 2 to Tier 1. Also manual.

## One-time setup

### 1. Anthropic API key

Get a key from https://console.anthropic.com. Keep it handy.

### 2. Google Cloud project for Gmail

1. Go to https://console.cloud.google.com and create a new project (or pick an existing one).
2. Enable the **Gmail API**.
3. Configure the OAuth consent screen as **External**, then add yourself (`samfoxanu@gmail.com`) as a Test User.
4. Create an **OAuth client ID** of type **Desktop application**. Download the JSON file.

### 3. Get a Gmail refresh token

Locally (on your laptop, not in CI), do this once:

```bash
git clone <this repo>
cd opportunities-newsletter-bot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Save the downloaded OAuth JSON as `credentials.json` in this folder.
python gmail_auth.py
```

A browser window opens. Grant Gmail compose/send/read access. The script prints your client ID, client secret, and refresh token to the terminal. Copy them.

### 4. Add GitHub secrets

In the GitHub repo: **Settings → Secrets and variables → Actions → New repository secret**. Add:

| Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `GMAIL_CLIENT_ID` | From the printed output |
| `GMAIL_CLIENT_SECRET` | From the printed output |
| `GMAIL_REFRESH_TOKEN` | From the printed output |
| `SAM_EMAIL` | `samfoxanu@gmail.com` |

### 5. Push and enable

Push the repo to GitHub. The workflow runs automatically on the first Monday of every month. You can also trigger it manually from the **Actions** tab → **Monthly Opportunities Newsletter Draft** → **Run workflow**.

## Running locally

For testing or one-off drafts:

```bash
cp .env.example .env       # then fill in your secrets
set -a; source .env; set +a
python agent.py
```

The Gmail draft will appear in your Drafts folder; the spreadsheet will be in `output/`.

## Cost

Each run uses Claude Sonnet to fetch ~25–50 URLs and emit a structured payload. Expect roughly **$1–$3 in API costs per monthly run**. GitHub Actions free tier easily covers a monthly job.

## When to update the skill

Edit files in `skill/references/`:

- **Add a new organisation**: edit `organisations.md` and place it under the appropriate tier.
- **Add a new verification trap**: edit `known-traps.md`.
- **Change the email template** (intro, opt-out wording, signup link): edit `template.md`.
- **Change spreadsheet columns**: edit `spreadsheet-schema.md` AND the `build_spreadsheet` function in `agent.py`.

Commit and push. The next run picks up the changes.

## Honest limitations

- **Verification will sometimes be wrong.** Pages get stale, deadlines shift mid-cycle, and the agent's reading of "is this still open" is a judgment call. The skill's `known-traps.md` covers the worst offenders, but expect ~1 borderline call per draft. That's why this saves as a draft, not sends.
- **Web fetching is text-only.** The fetcher strips HTML; it cannot click, log in, follow forms, or render JavaScript. Most think tank pages are static enough that this works, but a few orgs (e.g. anything behind a Cloudflare challenge) may fail. The agent will note these in its output.
- **The agent doesn't know which orgs are *new*.** If you want a brand-new organisation in the next newsletter, add it to `organisations.md` first.

## File map

```
.
├── README.md                   # this file
├── requirements.txt            # Python deps
├── agent.py                    # the bot
├── gmail_auth.py               # one-time OAuth helper
├── .env.example                # local env vars template
├── .gitignore
├── .github/
│   └── workflows/
│       └── monthly-newsletter.yml
└── skill/                      # mirrors the Claude skill
    ├── SKILL.md
    └── references/
        ├── organisations.md
        ├── template.md
        ├── spreadsheet-schema.md
        └── known-traps.md
```
