# Spreadsheet Schema

Every "More Opportunities!" newsletter is accompanied by an Excel spreadsheet (`.xlsx`) listing every currently-open program. The spreadsheet uses a fixed column structure so subscribers can filter on country, type, and other attributes.

## File naming

`more-opportunities-YYYY-MM-DD.xlsx` (use the send date, not the day of generation).

## Columns

| # | Column name | Type | Allowed values / notes |
|---|---|---|---|
| 1 | Country | Text | Country name (e.g. "Australia", "United Kingdom", "United States", "Global / Online") |
| 2 | Organisation | Text | Full name (e.g. "Institute of Economic Affairs"). No abbreviations in this column. |
| 3 | Program name | Text | Specific program (e.g. "General Internship", "Hayek Internship — Autumn term") |
| 4 | Type | Fixed list with "Other" fallback | Internship, Conference, Fellowship, Essay competition, Online course, Seminar, Scholarship, Other |
| 5 | Deadline | Text | A specific date in `DD Mon YYYY` format (e.g. "15 May 2026"), or one of: "Rolling", "Apply early", "Contact for window", "Applications open". Never invent a deadline. |
| 6 | Duration | Text | e.g. "12 weeks", "3 months", "4 days", "Semester", "Rolling — varies". Leave blank if not clearly specified on the live page. |
| 7 | Paid? | Text | "Yes — $18.50/hr" or "Yes — £1,000 stipend" or "Stipend only" or "No". Be specific about currency. |
| 8 | International eligibility | Fixed list | "Yes" / "No" / "Some restrictions" |
| 9 | Notes | Text (optional) | Use to expand on eligibility restrictions, visa sponsorship, language requirements, or other key caveats. Keep under one sentence. |
| 10 | Apply URL | URL | Direct link to the application page (not the org homepage) |

## Rules

- **Only currently-open programs** are listed. Closed programs and not-yet-opened programs are excluded.
- **One row per program** (not per organisation). The IEA, for example, gets multiple rows for General Internship, Media Internship, EPICENTER, FTL Undergraduate, etc.
- **No political affiliation column.** Self-labels are contested and Sam wants to avoid forcing labels on organisations that describe themselves as non-partisan.
- **Sort order**: Country (Australia first, then New Zealand, UK, Europe, US, Canada, Asia, Latin America, MENA, Africa, Global/Online), then by Type within each country.
- **Header row**: Bold the header row and freeze the top row so filters work cleanly.
- **Filters**: Enable Excel auto-filter on the header row so readers can filter by Country, Type, International eligibility, etc.

## Implementation

Use the xlsx skill at `/mnt/skills/public/xlsx/SKILL.md` to generate the file. Save to `/mnt/user-data/outputs/more-opportunities-YYYY-MM-DD.xlsx` and share with `present_files`.

## Example rows

```
Country         | Organisation                | Program name                          | Type        | Deadline       | Duration  | Paid?            | International eligibility | Notes                                   | Apply URL
United States   | Heritage Foundation         | Young Leaders Program (Fall 2026)     | Internship  | 31 May 2026    | 12–15 wks | Yes — $18.50/hr  | Some restrictions          | Must have US work authorisation         | https://www.heritage.org/young-leaders-program
United Kingdom  | Institute of Economic Affairs | General Internship (Autumn 2026)    | Internship  | 14 Aug 2026    | 3 months  | No               | Some restrictions          | Travel within M25 reimbursed; no visa   | https://iea.org.uk/students/iea-internship/
Global / Online | Hillsdale College           | Online Courses                        | Online course | Rolling      | Self-paced | No              | Yes                        | 40+ free courses; certificate available | https://online.hillsdale.edu/courses
```
