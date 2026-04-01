"""
Phrontis Financial - Separation Readiness Brief Generator
Calls Anthropic Claude API to generate a personalized weekly brief
"""

import os
import anthropic
from datetime import datetime, date
from dotenv import load_dotenv

load_dotenv()

SEPARATION_DATE = date(2027, 8, 1)


def days_to_separation():
    return (SEPARATION_DATE - date.today()).days


def generate_brief(client_data: dict) -> str:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""You are a military financial readiness analyst at Phrontis Financial.
    Generate a weekly separation readiness brief for this servicemember:

    {client_data}

    Days to separation: {days_to_separation()}

    Format the brief exactly as:
    PHRONTIS FINANCIAL - WEEKLY BRIEF
    Date: [today]
    Financial Readiness Score: [X]/100

    CRITICAL ACTIONS THIS WEEK:
    [numbered list, max 3]

    UPCOMING DECISION WINDOWS:
    [numbered list, max 3]

    MARKET INTELLIGENCE:
    [2 sentences on relevant financial conditions]

    YOUR TRAJECTORY:
    [2 sentences on projected financial position at separation]

    Powered by Phrontis Financial | Built by a Space Force Guardian"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


if __name__ == "__main__":
    demo_client = {
        "name": "LTC David Parker",
        "branch": "Space Force",
        "pay_grade": "O-5",
        "years_of_service": 12,
        "tsp_balance": 387000,
        "pension_eligible": True,
        "sbp_decision_made": False,
        "va_claim_filed": False,
        "arktyx_83b_filed": False,
        "llc_monthly_revenue": 8500,
        "spouse_income": 94000
    }

    brief = generate_brief(demo_client)
    print(brief)
