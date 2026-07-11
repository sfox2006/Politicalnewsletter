"""
One-time helper: run this LOCALLY (not in CI) to get your Gmail refresh token.

Prereqs:
  1. Create a Google Cloud project (https://console.cloud.google.com).
  2. Enable the Gmail API.
  3. Configure OAuth consent screen as "External" and add yourself as a test user.
  4. Create an OAuth client ID (Desktop application). Download the JSON.
  5. Save it next to this file as `credentials.json`.

Then:
  python gmail_auth.py

It will open a browser, ask you to grant Gmail compose/send/read access,
and then print a refresh token. Add it to your GitHub secrets as
GMAIL_REFRESH_TOKEN. Also add GMAIL_CLIENT_ID and GMAIL_CLIENT_SECRET from
the credentials.json file.
"""
import json
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def main():
    creds_path = Path("credentials.json")
    if not creds_path.exists():
        raise SystemExit("credentials.json not found. See instructions at the top of this file.")

    flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
    creds = flow.run_local_server(
        port=0,
        access_type="offline",
        prompt="consent",
        include_granted_scopes="true",
    )

    with creds_path.open() as f:
        client_info = json.load(f)["installed"]

    output = "\n".join([
        "=== Add these as GitHub repo secrets ===",
        f"GMAIL_CLIENT_ID={client_info['client_id']}",
        f"GMAIL_CLIENT_SECRET={client_info['client_secret']}",
        f"GMAIL_REFRESH_TOKEN={creds.refresh_token}",
        "",
        "Also add:",
        "ANTHROPIC_API_KEY=<your Anthropic API key>",
        "SAM_EMAIL=samfoxanu@gmail.com   (or whichever Gmail you want drafts in)",
        "",
    ])

    Path("gmail_secrets.txt").write_text(output, encoding="utf-8")
    print("\n\n" + output)
    print("Saved the same values to gmail_secrets.txt in this folder.")


if __name__ == "__main__":
    main()
