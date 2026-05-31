def rule_engine(txn):
    rules = []

    if txn["amount"] > 5000:
        rules.append("HIGH_AMOUNT")

    if txn["country"] != txn["user_country"]:
        rules.append("GEO_MISMATCH")

    return rules