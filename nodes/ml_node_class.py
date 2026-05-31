from tools.ml_tool import ml_score

def ml_node(state):
    score = ml_score(state["txn"])
    return {"ml_score": score}