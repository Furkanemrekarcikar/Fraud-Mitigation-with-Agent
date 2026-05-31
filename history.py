user_memory = {}

def get_user_history(user_id):
    return user_memory.get(user_id, [])

def update_user_memory(user_id, txn, decision):
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append({
        "txn": txn,
        "decision": decision
    })