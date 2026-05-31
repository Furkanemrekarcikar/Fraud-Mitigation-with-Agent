from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

@tool
def get_ml_score(txn_data: dict) -> float:
    """
    işlemin Kaggle verisetine göre makine öğrenmesi risk skorunu hesaplar
    Kullanıcının risk skorunu sayısal olarak görmek istediğinde kullanılmalı
    """
    return 0.85


@tool
def check_rules(amount: float, user_country: str, txn_country: str) -> list:
    """
    İşlemin banka ve iş kurallarını ihlal edip etmediğini kontrol edder
    tutar yüksekse veya ülkeler farklıysa banka kurallarını test etmek için kullanılır
    """

    return ["GEO_MISMATCH"]


@tool
def check_graph_network(user_id: str, merchant_id: str) -> int:
    """
    Kullanıcı ve satıcı arasındaki sosyal ağ dolandırıcılık bağlarını kontrol eder.
    Kullanıcının satıcıyla geçmiş bir bağı olup olmadığını anlamak için kullanılır
    """
    return 1


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tool_list = [get_ml_score, check_rules, check_graph_network]
agent_executor = create_react_agent(llm, tool_list)


if __name__ == "__main__":

    user_prompt = """
    Elimde bir işlem var. Kullanıcı ID'si U-1453. İşlem Türkiye'de (TR) yapılıyor ama 
    kullanıcı ABD'de (US) yaşıyor. Miktar 7500 dolar. Satıcı M-9999.
    Bu işlem sence dolandırıcılık mı? Karar vermek için elindeki araçları kullan.
    """


    print("ajan düşünüyor\n")

    for chunk in agent_executor.stream({"messages": [("user", user_prompt)]}):
        if "agent" in chunk:
            print(f"Ajan cevabı: {chunk['agent']['messages'][0].content}")
        elif "tools" in chunk:
            print(f"tools is called: {chunk['tools']['messages'][0].name}")