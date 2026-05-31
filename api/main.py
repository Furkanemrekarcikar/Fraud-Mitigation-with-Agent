from fastapi import FastAPI
from pydantic import BaseModel
from workflow import graph

app = FastAPI(title="Fraud Detection API")

class Transaction(BaseModel):
    user_id: str
    merchant_id: str
    amount: float
    timestamp: str
    country: str
    user_country: str

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running"}

@app.post("/analyze")
def analyze(txn: Transaction):
    txn_dict = txn.model_dump()

    result = graph.invoke({
        "txn": txn_dict
    })

    return {
        "decision": result.get("decision"),
        "reasoning": result.get("reasoning"),
        "signals": {
            "ml_score": result.get("ml_score"),
            "rules": result.get("rules"),
            "graph_score": result.get("graph_score")
        }
    }