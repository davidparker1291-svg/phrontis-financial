"""
Phrontis Financial - PCS Financial Analyzer Agent
Compares BAH rates between duty stations and provides VA loan guidance.
"""


BAH_RATES_2026 = {
    "Fort Liberty": {"E-5": 1350, "O-3": 1677, "O-5": 1956},
    "Fort Cavazos": {"E-5": 1287, "O-3": 1608, "O-5": 1884},
    "Fort Campbell": {"E-5": 1206, "O-3": 1518, "O-5": 1785},
    "Fort Stewart": {"E-5": 1281, "O-3": 1602, "O-5": 1878},
    "Joint Base Lewis-McChord": {"E-5": 1734, "O-3": 2079, "O-5": 2373},
    "Fort Drum": {"E-5": 1254, "O-3": 1569, "O-5": 1842},
    "Fort Carson": {"E-5": 1650, "O-3": 1986, "O-5": 2271},
    "Fort Bliss": {"E-5": 1257, "O-3": 1575, "O-5": 1845},
    "Fort Riley": {"E-5": 1110, "O-3": 1398, "O-5": 1650},
    "Fort Moore": {"E-5": 1233, "O-3": 1548, "O-5": 1818},
    "Fort Sill": {"E-5": 1101, "O-3": 1389, "O-5": 1641},
    "Camp Pendleton": {"E-5": 2280, "O-3": 2712, "O-5": 3069},
    "Camp Lejeune": {"E-5": 1245, "O-3": 1560, "O-5": 1830},
    "Norfolk": {"E-5": 1479, "O-3": 1824, "O-5": 2106},
    "San Diego": {"E-5": 2400, "O-3": 2862, "O-5": 3234},
    "Pearl Harbor": {"E-5": 2604, "O-3": 3102, "O-5": 3504},
    "Jacksonville": {"E-5": 1380, "O-3": 1713, "O-5": 1995},
    "Pensacola": {"E-5": 1305, "O-3": 1629, "O-5": 1905},
    "Washington DC": {"E-5": 2265, "O-3": 2700, "O-5": 3054},
    "Peterson SFB": {"E-5": 1650, "O-3": 1986, "O-5": 2271},
    "Buckley SFB": {"E-5": 1911, "O-3": 2286, "O-5": 2604},
    "Vandenberg SFB": {"E-5": 1950, "O-3": 2334, "O-5": 2658},
    "Patrick SFB": {"E-5": 1455, "O-3": 1800, "O-5": 2082},
    "Los Angeles AFB": {"E-5": 2640, "O-3": 3147, "O-5": 3561},
    "Schriever SFB": {"E-5": 1650, "O-3": 1986, "O-5": 2271},
    "Eglin AFB": {"E-5": 1353, "O-3": 1683, "O-5": 1962},
    "Travis AFB": {"E-5": 2100, "O-3": 2508, "O-5": 2850},
    "Langley AFB": {"E-5": 1479, "O-3": 1824, "O-5": 2106},
    "MacDill AFB": {"E-5": 1500, "O-3": 1854, "O-5": 2142},
    "Fort Meade": {"E-5": 1890, "O-3": 2265, "O-5": 2583},
    "Fort Eisenhower": {"E-5": 1179, "O-3": 1485, "O-5": 1752},
    "Schofield Barracks": {"E-5": 2604, "O-3": 3102, "O-5": 3504},
    "Fort Wainwright": {"E-5": 1422, "O-3": 1764, "O-5": 2049},
    "Fort Huachuca": {"E-5": 1104, "O-3": 1392, "O-5": 1644},
    "Nellis AFB": {"E-5": 1596, "O-3": 1920, "O-5": 2199},
    "Luke AFB": {"E-5": 1476, "O-3": 1797, "O-5": 2067},
    "Hill AFB": {"E-5": 1350, "O-3": 1656, "O-5": 1929},
    "Offutt AFB": {"E-5": 1320, "O-3": 1620, "O-5": 1890},
    "Tinker AFB": {"E-5": 1233, "O-3": 1524, "O-5": 1782},
    "Fort Bragg": {"E-5": 1350, "O-3": 1677, "O-5": 1956},
    "Fort Hood": {"E-5": 1287, "O-3": 1608, "O-5": 1884},
    "Fort Benning": {"E-5": 1233, "O-3": 1548, "O-5": 1818},
    "Fort Gordon": {"E-5": 1179, "O-3": 1485, "O-5": 1752},
    "Kadena AB": {"E-5": 1800, "O-3": 2100, "O-5": 2400},
    "Ramstein AB": {"E-5": 1650, "O-3": 1950, "O-5": 2250},
    "Camp Humphreys": {"E-5": 1700, "O-3": 2000, "O-5": 2300},
    "Yokota AB": {"E-5": 1750, "O-3": 2050, "O-5": 2350},
    "Fort Shafter": {"E-5": 2604, "O-3": 3102, "O-5": 3504},
    "Joint Base San Antonio": {"E-5": 1362, "O-3": 1686, "O-5": 1968},
    "Joint Base Andrews": {"E-5": 2265, "O-3": 2700, "O-5": 3054},
}


def find_station(name: str) -> tuple[str, dict] | None:
    """Fuzzy match a station name against the BAH table."""
    name_lower = name.strip().lower()
    for station, rates in BAH_RATES_2026.items():
        if name_lower in station.lower() or station.lower() in name_lower:
            return station, rates
    return None


def analyze_pcs(
    current_station: str,
    gaining_station: str,
    grade: str = "E-5",
    va_loan_status: str = "never_used",
) -> dict:
    """
    Analyze PCS financial impact between two duty stations.

    Args:
        current_station: Name of current duty station
        gaining_station: Name of gaining duty station
        grade: Pay grade (E-5, O-3, or O-5)
        va_loan_status: never_used, currently_using, or full_entitlement

    Returns:
        Dict with BAH comparison, VA loan recommendation, and financial summary.
    """
    current = find_station(current_station)
    gaining = find_station(gaining_station)

    current_name = current[0] if current else current_station
    gaining_name = gaining[0] if gaining else gaining_station
    current_bah = current[1].get(grade, 1400) if current else 1400
    gaining_bah = gaining[1].get(grade, 1400) if gaining else 1400

    delta = gaining_bah - current_bah
    annual_delta = delta * 12

    va_recommendation = _va_loan_recommendation(va_loan_status, gaining_name)

    return {
        "current_station": current_name,
        "gaining_station": gaining_name,
        "grade": grade,
        "current_bah": current_bah,
        "gaining_bah": gaining_bah,
        "monthly_delta": delta,
        "annual_delta": annual_delta,
        "va_loan": va_recommendation,
    }


def _va_loan_recommendation(status: str, gaining: str) -> dict:
    """Generate VA loan recommendation based on entitlement status."""
    if status in ("never_used", "full_entitlement"):
        return {
            "status": "Full entitlement available",
            "recommendation": f"Strong candidate for VA loan at {gaining}",
            "down_payment": "$0",
            "funding_fee": "2.15% first use (waived if VA disabled)",
        }
    return {
        "status": "Currently in use",
        "recommendation": "Consider selling current home or using second-tier entitlement",
        "down_payment": "May require down payment for second-tier",
        "funding_fee": "3.3% subsequent use",
    }


if __name__ == "__main__":
    result = analyze_pcs(
        current_station="Fort Liberty",
        gaining_station="Joint Base Lewis-McChord",
        grade="E-5",
        va_loan_status="never_used",
    )
    print(f"PCS: {result['current_station']} -> {result['gaining_station']}")
    print(f"BAH: ${result['current_bah']:,} -> ${result['gaining_bah']:,}")
    print(f"Monthly Delta: ${result['monthly_delta']:+,}")
    print(f"Annual Delta: ${result['annual_delta']:+,}")
    print(f"\nVA Loan: {result['va_loan']['recommendation']}")
