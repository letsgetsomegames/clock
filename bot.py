import openai
import os

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key as a string: 'your-api-key'

def chat_with_gpt():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("ChatGPT is ready! Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or use "gpt-3.5-turbo" if you prefer
                messages=messages
            )

            reply = response['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": reply})
            print(f"ChatGPT: {reply}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gpt()
