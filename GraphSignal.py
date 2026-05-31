import networkx as nx

G = nx.Graph()

def update_graph(user_id, merchant_id):
    G.add_edge(user_id, merchant_id)

def graph_risk_score(user_id):
    neighbors = list(G.neighbors(user_id))

    return len(neighbors)