import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "phi3"

def chat():
    messages = []

    print("🤖 Ollama Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": messages,
                "stream": False  
            }
        )

        data = response.json()
        
        data = response.json()
        reply = data["message"]["content"]

        print("Bot:", reply)

        messages.append({"role": "assistant", "content": reply})
        

if __name__ == "__main__":
    chat()