"""
Phrontis Financial - TSP Roth vs Traditional Calculator
Models tax-advantaged scenarios for military separation planning
"""

from datetime import date

SEPARATION_DATE = date(2027, 8, 1)


def years_to_separation():
    delta = SEPARATION_DATE - date.today()
    return max(delta.days / 365.25, 0)


def project_tsp(current_balance, annual_contribution, annual_return, years):
    balance = current_balance
    monthly_return = (1 + annual_return) ** (1 / 12) - 1
    monthly_contribution = annual_contribution / 12
    for _ in range(int(years * 12)):
        balance = balance * (1 + monthly_return) + monthly_contribution
    return round(balance, 2)


def roth_vs_traditional(
    trad_balance,
    roth_balance,
    annual_contribution,
    annual_return,
    current_tax_rate,
    retirement_tax_rate,
    years=None
):
    if years is None:
        years = years_to_separation()

    trad_projected = project_tsp(trad_balance, annual_contribution, annual_return, years)
    roth_projected = project_tsp(roth_balance, annual_contribution, annual_return, years)

    trad_after_tax = trad_projected * (1 - retirement_tax_rate)
    roth_after_tax = roth_projected

    roth_advantage = roth_after_tax - trad_after_tax

    return {
        "years_to_separation": round(years, 1),
        "traditional": {
            "current": trad_balance,
            "projected": trad_projected,
            "after_tax_value": round(trad_after_tax, 2),
            "tax_rate_at_withdrawal": retirement_tax_rate
        },
        "roth": {
            "current": roth_balance,
            "projected": roth_projected,
            "after_tax_value": round(roth_after_tax, 2),
            "tax_rate_at_withdrawal": 0
        },
        "roth_advantage": round(roth_advantage, 2),
        "recommendation": "Roth" if roth_advantage > 0 else "Traditional"
    }


if __name__ == "__main__":
    result = roth_vs_traditional(
        trad_balance=290000,
        roth_balance=97000,
        annual_contribution=23000,
        annual_return=0.07,
        current_tax_rate=0.24,
        retirement_tax_rate=0.28
    )
    print("TSP OPTIMIZER RESULTS")
    print("=" * 50)
    print(f"Years to separation: {result['years_to_separation']}")
    print(f"\nTraditional TSP:")
    print(f"  Current: ${result['traditional']['current']:,.2f}")
    print(f"  Projected at separation: ${result['traditional']['projected']:,.2f}")
    print(f"  After-tax value: ${result['traditional']['after_tax_value']:,.2f}")
    print(f"\nRoth TSP:")
    print(f"  Current: ${result['roth']['current']:,.2f}")
    print(f"  Projected at separation: ${result['roth']['projected']:,.2f}")
    print(f"  After-tax value: ${result['roth']['after_tax_value']:,.2f}")
    print(f"\nRoth advantage: ${result['roth_advantage']:,.2f}")
    print(f"Recommendation: {result['recommendation']}")
