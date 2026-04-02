"""
Phrontis Financial - VA Disability Optimizer Agent
Calculates estimated VA combined rating and benefit projections.
"""


VA_RATES_2026 = {
    0: 0,
    10: 171,
    20: 338,
    30: 524,
    40: 755,
    50: 1075,
    60: 1361,
    70: 1716,
    80: 1995,
    90: 2241,
    100: 3737,
}

CONDITION_RATINGS = {
    "hearing_loss_tinnitus": 10,
    "back_spine": 20,
    "ptsd_mental_health": 30,
    "sleep_apnea": 50,
    "knee_joints": 10,
    "tbi": 40,
    "burn_pit_toxic_exposure": 10,
    "respiratory": 10,
    "hypertension": 10,
    "diabetes": 20,
    "mst_related": 30,
}


def va_combined_rating(ratings: list[int]) -> int:
    """Calculate VA combined disability rating using VA math."""
    sorted_ratings = sorted(ratings, reverse=True)
    combined = 0.0
    for r in sorted_ratings:
        pct = r / 100.0
        combined = combined + pct * (1 - combined)
    return round(combined * 100 / 10) * 10


def estimate_rating(conditions: dict[str, str]) -> dict:
    """
    Takes a dict of condition_name -> status (Yes/No/Unsure).
    Returns estimated rating range and benefit projections.
    """
    confirmed = []
    possible = []

    for condition, status in conditions.items():
        base_rating = CONDITION_RATINGS.get(condition, 10)
        if status == "Yes":
            confirmed.append(base_rating)
        elif status == "Unsure":
            possible.append(base_rating)

    low_ratings = list(confirmed)
    high_ratings = list(confirmed) + list(possible)

    low_combined = va_combined_rating(low_ratings) if low_ratings else 0
    high_combined = va_combined_rating(high_ratings) if high_ratings else 0

    low_monthly = VA_RATES_2026.get(low_combined, 0)
    high_monthly = VA_RATES_2026.get(high_combined, 0)

    return {
        "low_rating": low_combined,
        "high_rating": high_combined,
        "low_monthly": low_monthly,
        "high_monthly": high_monthly,
        "low_lifetime_25yr": low_monthly * 12 * 25,
        "high_lifetime_25yr": high_monthly * 12 * 25,
        "conditions_claimed": len(confirmed) + len(possible),
        "next_steps": _generate_next_steps(conditions, low_combined),
    }


def _generate_next_steps(conditions: dict, current_rating: int) -> list[str]:
    """Generate personalized next steps based on conditions."""
    steps = []
    steps.append(
        "Connect with a Veterans Service Organization (VSO) for free claim assistance"
    )

    if conditions.get("ptsd_mental_health") in ("Yes", "Unsure"):
        steps.append(
            "Schedule a mental health evaluation - PTSD claims benefit from documented treatment history"
        )
    if conditions.get("burn_pit_toxic_exposure") in ("Yes", "Unsure"):
        steps.append(
            "Register with the VA Burn Pit Registry and file under PACT Act presumptives"
        )
    if conditions.get("sleep_apnea") in ("Yes", "Unsure"):
        steps.append(
            "Get a sleep study ordered - sleep apnea is one of the highest-rated individual conditions"
        )

    steps.append(
        "Gather service medical records and buddy statements for all claimed conditions"
    )
    steps.append(
        "File your claim before separation for fastest processing (BDD program if 90-180 days out)"
    )

    return steps


if __name__ == "__main__":
    sample_conditions = {
        "hearing_loss_tinnitus": "Yes",
        "back_spine": "Yes",
        "ptsd_mental_health": "Yes",
        "sleep_apnea": "Unsure",
        "knee_joints": "Yes",
        "tbi": "No",
        "burn_pit_toxic_exposure": "Yes",
        "respiratory": "No",
        "hypertension": "No",
        "diabetes": "No",
        "mst_related": "No",
    }

    result = estimate_rating(sample_conditions)
    print(f"Estimated Rating Range: {result['low_rating']}% - {result['high_rating']}%")
    print(
        f"Monthly Benefit: ${result['low_monthly']:,} - ${result['high_monthly']:,}"
    )
    print(
        f"Lifetime Value (25yr): ${result['low_lifetime_25yr']:,} - ${result['high_lifetime_25yr']:,}"
    )
    print("\nNext Steps:")
    for i, step in enumerate(result["next_steps"], 1):
        print(f"  {i}. {step}")
