# Phrontis Financial — AI Agents

Python-based AI agents for military financial separation planning.

## separation_brief.py

Generates a weekly separation readiness brief using the Anthropic Claude API.

### Setup

```bash
cd agents
pip install -r requirements.txt
```

### Configuration

Copy `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

### Run

```bash
python separation_brief.py
```

## tsp_optimizer.py

TSP Roth vs Traditional calculator that models tax-advantaged scenarios for military separation planning.

### Run

```bash
python tsp_optimizer.py
```

No API key required — runs locally with pure math.
