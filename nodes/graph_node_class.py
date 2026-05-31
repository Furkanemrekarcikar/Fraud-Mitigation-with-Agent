from tools.graph_tool import graph_score
from GraphSignal import update_graph


def graph_node(state):
    user_id = state["txn"]["user_id"]
    merchant_id = state["txn"]["merchant_id"]

    update_graph(user_id, merchant_id)
    score = graph_score(user_id)

    return {"graph_score": score}