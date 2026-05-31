from typing import TypedDict

class GraphState(TypedDict):
    txn: dict
    ml_score: float
    rules: list
    graph_score: float
    decision: str
    reasoning: str