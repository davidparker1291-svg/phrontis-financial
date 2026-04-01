# Phrontis Financial

The AI-powered financial operating system built for servicemembers transitioning to civilian life. Phrontis Financial connects TSP optimization, pension timing, SBP elections, VA benefits, and separation planning into a single intelligent platform — backed by AI analysis and reviewed by a credentialed CFP with military financial expertise.

Co-founded by David Parker (U.S. Space Force Guardian, 12+ years active duty, MBA Northwestern Kellogg, separating August 2027) and Jordan (CFP, Army veteran). Built for the 200,000 servicemembers who separate each year without a connected financial plan.

## Stack

- **Frontend:** Static HTML/CSS, dark navy design system, Arial typography
- **AI Agents:** Python + Anthropic Claude API
- **Hosting:** Netlify (static site + forms)
- **Charts:** Chart.js via cdnjs.cloudflare.com
- **Payments:** Stripe (coming soon)
- **Notifications:** Twilio SMS (coming soon)

## File Map

| File | Purpose |
|------|---------|
| `index.html` | Public landing page — hero, pricing, lead form |
| `dashboard.html` | DP's personal separation dashboard (password: `PFCommand2026!`) |
| `jordan.html` | CFP practice demo for Jordan (password: `GarrisonCFP2026!`) |
| `subscribe.html` | Subscription tier page with waitlist form |
| `success.html` | Form submission confirmation |
| `agents/separation_brief.py` | AI separation readiness brief generator |
| `agents/tsp_optimizer.py` | TSP Roth vs Traditional calculator |
| `agents/requirements.txt` | Python dependencies |
| `agents/.env` | API keys (gitignored) |
| `netlify.toml` | Netlify build config + redirects + headers |
| `_redirects` | Netlify redirect rules |

## Running the AI Agents

```bash
cd agents
pip install -r requirements.txt

# Update .env with your Anthropic API key
# ANTHROPIC_API_KEY=sk-ant-...

python separation_brief.py   # Generates weekly AI brief
python tsp_optimizer.py       # Runs TSP Roth vs Traditional analysis
```

## Netlify Deployment

1. Connect GitHub repo to Netlify
2. Build command: (none — static site)
3. Publish directory: `.`
4. Forms are auto-detected via `data-netlify="true"`

## GitHub Repository

`davidparker1291-svg/phrontis-financial`

## Dashboard Passwords

- **Separation Command (DP):** `PFCommand2026!`
- **CFP Command Center (Jordan):** `GarrisonCFP2026!`

## Next Build Priorities

1. RevenueCat/Stripe live payment integration
2. Twilio weekly brief SMS delivery
3. Jordan co-founder onboarding and equity structure
4. Mobile-responsive refinements
5. Client self-service onboarding flow
