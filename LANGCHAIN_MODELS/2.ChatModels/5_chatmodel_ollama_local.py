from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3"
)

result = model.invoke("What is the capital of India?")

print(result.content)
