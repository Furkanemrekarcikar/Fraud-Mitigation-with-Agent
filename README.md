# Fraud Mitigation with Agent

A multi-signal fraud detection system that combines machine learning, rule-based checks, graph analysis, and an LLM decision agent in a unified LangGraph pipeline.

## How It Works

Each transaction flows through a four-stage pipeline:

```
ML Score → Rule Engine → Graph Signal → LLM Decision
```

| Stage | What it does |
|---|---|
| **ML Node** | XGBoost model predicts fraud probability from transaction features |
| **Rule Node** | Checks business rules (high amount, geographic mismatch) |
| **Graph Node** | Scores user-merchant relationship risk via network analysis |
| **LLM Node** | GPT-4o-mini synthesizes all signals and returns APPROVE / REVIEW / REJECT |

## Project Structure

```
├── api/
│   └── main.py              # FastAPI REST endpoint
├── agent/
│   └── llm_decision_agent.py
├── nodes/
│   ├── ml_node_class.py
│   ├── rule_node_class.py
│   ├── graph_node_class.py
│   └── llm_node_class.py
├── tools/
│   ├── ml_tool.py
│   ├── rule_tool.py
│   └── graph_tool.py
├── workflow.py              # LangGraph pipeline definition
├── state.py                 # Shared pipeline state schema
├── mLmodel.py               # XGBoost training script
├── RuleEngine.py            # Rule definitions
├── GraphSignal.py           # NetworkX graph logic
├── REACT_EXAMPLE.py         # Standalone ReAct agent example
└── fraud_model.pkl          # Trained model (not in repo)
```

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_key_here
```

## Train the Model

Download the [Kaggle Credit Card Fraud dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) as `creditcard.csv`, then run:

```bash
python mLmodel.py
```

This generates `fraud_model.pkl`.

## Run the API

```bash
uvicorn api.main:app --reload
```

### Example Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "U-1453",
    "merchant_id": "M-9999",
    "amount": 7500,
    "timestamp": "2024-01-15T14:30:00",
    "country": "TR",
    "user_country": "US"
  }'
```

### Example Response

```json
{
  "decision": "REJECT",
  "reasoning": "High transaction amount with geographic mismatch. ML score indicates elevated fraud probability.",
  "signals": {
    "ml_score": 0.91,
    "rules": ["HIGH_AMOUNT", "GEO_MISMATCH"],
    "graph_score": 1
  }
}
```

## ReAct Agent Example

`REACT_EXAMPLE.py` demonstrates a standalone LangChain ReAct agent that uses the same tools interactively:

```bash
python REACT_EXAMPLE.py
```

## Tech Stack

- **LangGraph** — pipeline orchestration
- **XGBoost** — fraud probability scoring
- **NetworkX** — user-merchant graph analysis
- **LangChain + GPT-4o-mini** — final decision reasoning
- **FastAPI** — REST API
