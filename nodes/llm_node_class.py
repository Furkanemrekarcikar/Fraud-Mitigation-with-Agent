from pydantic import BaseModel, Field
from history import get_user_history, update_user_memory
from agent.llm_decision_agent import agent

class FraudDecision(BaseModel):
    decision: str = Field(description="Only APPROVE, REVIEW, or REJECT")
    reasoning: str = Field(description="A brief explanation of why this decision was made")

def llm_node(GraphState):
    user_id = GraphState["txn"]["user_id"]
    history = get_user_history(user_id)

    prompt = f"""
    You are a fraud detection decision engine.

    USER HISTORY:
    {history}

    CURRENT TRANSACTION:
    {GraphState["txn"]}

    ML SCORE: {GraphState["ml_score"]}
    RULES: {GraphState["rules"]}
    GRAPH SCORE: {GraphState["graph_score"]}

    Analyze the data and provide your decision and reasoning.
    """

    structured_llm = agent.with_structured_output(FraudDecision)
    response = structured_llm.invoke(prompt)

    GraphState["decision"] = response.decision
    GraphState["reasoning"] = response.reasoning

    update_user_memory(user_id, GraphState["txn"], response.decision)

    return GraphState