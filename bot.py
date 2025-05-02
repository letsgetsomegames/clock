import openai
import os

# Set your API key here or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") or input("Enter your OpenAI API key: ")

def chat_with_jaquavion():
    print("🧠 Jaquavion: Yo, I'm Jaquavion. Ask me anything, fam. (Type 'exit' to bounce.)\n")
    
    conversation = [
        {"role": "system", "content": "You are Jaquavion, a witty, friendly chatbot with swagger. Keep responses helpful, fun, and slightly streetwise, unless told otherwise."}
    ]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🧠 Jaquavion: Aight, peace out! ✌️")
            break

        conversation.append({"role": "user", "content": user_input})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=conversation
            )
            
            reply = response['choices'][0]['message']['content']
            print(f"🧠 Jaquavion: {reply}")
            conversation.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    chat_with_jaquavion()
