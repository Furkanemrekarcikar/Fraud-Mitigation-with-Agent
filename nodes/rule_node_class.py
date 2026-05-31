from tools.rule_tool import rule_score

def rule_node(state):
    rules = rule_score(state["txn"])
    return {"rules": rules}