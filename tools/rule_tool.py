from RuleEngine import rule_engine

def rule_score(txn: dict):
    rules = rule_engine(txn)
    return rules