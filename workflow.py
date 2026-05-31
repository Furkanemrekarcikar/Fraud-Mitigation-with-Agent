from langgraph.graph import StateGraph
from nodes.ml_node_class import ml_node
from nodes.graph_node_class import graph_node
from nodes.llm_node_class import llm_node
from nodes.rule_node_class import rule_node
from state import GraphState


builder = StateGraph(GraphState)

builder.add_node("ml", ml_node)
builder.add_node("rules", rule_node)
builder.add_node("graph", graph_node)
builder.add_node("llm", llm_node)

builder.set_entry_point("ml")
builder.add_edge("ml", "rules")
builder.add_edge("rules", "graph")
builder.add_edge("graph", "llm")

graph = builder.compile()