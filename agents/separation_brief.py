"""
Phrontis Financial - Separation Readiness Brief Generator
Calls Anthropic Claude API to generate a personalized weekly brief.
Accepts full intake data dict from n8n webhook.
"""

import os
import anthropic
from datetime import datetime, date
from dotenv import load_dotenv

load_dotenv()


def days_until(separation_month: int, separation_year: int) -> int:
    """Calculate days until separation date."""
    try:
        sep_date = date(separation_year, separation_month, 1)
        return (sep_date - date.today()).days
    except (ValueError, TypeError):
        return 365


def generate_brief(intake_data: dict) -> str:
    """
    Generate a personalized separation brief from intake data.

    Args:
        intake_data: Full intake form data dict with keys:
            name, branch, grade, separation_month, separation_year,
            tsp_balance, brs, family, spouse_works, housing, equity,
            va_status, va_rating, concerns, phone, email, timezone, score

    Returns:
        SMS-ready brief text under 1600 characters.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    name = intake_data.get("name", "Service Member")
    branch = intake_data.get("branch", "")
    grade = intake_data.get("grade", "")
    sep_month = intake_data.get("separation_month", 1)
    sep_year = intake_data.get("separation_year", 2027)
    days = days_until(int(sep_month), int(sep_year))
    tsp = intake_data.get("tsp_balance", "Unknown")
    concerns = intake_data.get("concerns", "General planning")
    score = intake_data.get("score", 50)
    va_status = intake_data.get("va_status", "Not filed")
    family = intake_data.get("family", "")
    housing = intake_data.get("housing", "")

    prompt = f"""You are a military financial readiness analyst at Phrontis Financial.
Generate a weekly separation readiness brief for this servicemember.
The brief MUST be under 1600 characters total (SMS limit).

SERVICE MEMBER PROFILE:
- Name: {name}
- Branch: {branch}
- Grade: {grade}
- Days to separation: {days}
- TSP balance range: {tsp}
- VA status: {va_status}
- Family: {family}
- Housing: {housing}
- Top concerns: {concerns}
- Readiness score: {score}/100

Format the brief exactly as:
PHRONTIS BRIEF | {datetime.now().strftime('%b %d, %Y')}

{name}, you have {days} days until separation.

CRITICAL ACTIONS THIS WEEK:
[3 specific, actionable items based on their profile and timeline]

DECISION WINDOW:
[1 upcoming deadline or time-sensitive decision]

SCORE: {score}/100

Reply BRIEF for full report | CALL to schedule CFP

Keep it direct, military-style, no fluff. Under 1600 characters."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )

    brief = message.content[0].text

    if len(brief) > 1600:
        brief = brief[:1597] + "..."

    return brief


if __name__ == "__main__":
    demo_intake = {
        "name": "MAJ Webb",
        "branch": "U.S. Army",
        "grade": "O-4",
        "separation_month": 7,
        "separation_year": 2027,
        "tsp_balance": "$150K-$300K",
        "brs": "Yes",
        "family": "Married with children",
        "spouse_works": "Yes",
        "housing": "Yes VA loan",
        "equity": "$45,000",
        "va_status": "No planning to",
        "va_rating": "",
        "concerns": "TSP decisions, VA claim",
        "phone": "+15551234567",
        "email": "demo@example.com",
        "timezone": "ET",
        "score": 58,
    }

    brief = generate_brief(demo_intake)
    print(brief)
    print(f"\n--- Length: {len(brief)} chars ---")
