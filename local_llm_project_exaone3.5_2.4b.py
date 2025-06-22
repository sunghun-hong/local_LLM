## ollama run exaone3.5:7.8b
## ollama run exaone3.5:7.2.4b


from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 

llm = ChatOllama(model="exaone3.5:2.4b")

messages = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("User\t:").strip()

    if user_input in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=user_input))
    
    response = llm.invoke(messages)
    print("AI_Bot\t:", response.content)

    messages.append(AIMessage(response.content))
