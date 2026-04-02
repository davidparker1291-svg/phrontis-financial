# Phrontis Financial

The AI Financial Operating System built for the military life transition.

**Built by a Space Force Guardian. Powered by AI. Reviewed by a CFP.**

## Overview

200,000 servicemembers separate every year. Most leave money on the table. Phrontis Financial changes that by connecting TSP optimization, VA disability claims, pension timing, SBP elections, and separation planning into a single intelligent platform.

## Product Modules

| Module | Tier | Description |
|--------|------|-------------|
| Separation Command | All Tiers | Countdown with every financial milestone mapped |
| TSP Optimizer | All Tiers | Roth vs Traditional modeling for military pay |
| VA Disability Optimizer | Operator+ | AI-guided claim prep and benefit estimation |
| PCS Financial Command | Operator+ | BAH comparison, VA loan, buy vs rent analysis |
| Military Spouse Track | Operator+ | Financial independence planning for spouses |
| Separation War Room | Unit Command | 90-day intensive cohort with direct CFP access |
| Trading Command | Self-Directed | Investing education beyond TSP |

## Stack

- **Frontend:** Static HTML/CSS/JS — GitHub Pages
- **Styling:** Arial only, dark navy (#0a0e1a) + gold (#d4af37)
- **Data Layer:** Google Sheets via n8n webhooks
- **AI Agents:** Python + Anthropic Claude API
- **SMS:** Twilio for weekly brief delivery
- **CFP Partner:** Jordan, CFP, Army veteran

## File Structure

```
index.html          Landing page
intake.html         10-question onboarding flow
dashboard.html      Personalized financial dashboard
va-optimizer.html   VA Disability Optimizer (standalone)
pcs-command.html    PCS Financial Command tool
jordan.html         CFP practice dashboard (password protected)
subscribe.html      Pricing tiers + waitlist
success.html        Form success confirmation
404.html            Custom 404 page
CNAME               Custom domain config
agents/
  separation_brief.py   AI brief generator
  va_optimizer.py       VA rating calculator
  pcs_analyzer.py       BAH comparison engine
  requirements.txt      Python dependencies
  .env                  API keys (gitignored)
```

## Deployment

GitHub Pages via GitHub Actions. Push to `main` triggers automatic deploy.

## Company

**Phrontis Financial** — A Phrontis Holdings Company

Founded by David Parker, Space Force Guardian, Kellogg MBA.
CFP Partner: Jordan, CFP, Army veteran.

---

2026 Phrontis Financial LLC | Not financial advice. CFP services provided by independent practitioner.
