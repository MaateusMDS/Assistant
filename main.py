from dotenv import load_dotenv
import openai
import os

load_dotenv()

api_key = os.getenv('API_KEY')

openai.api_key = api_key
messages = [{"role": "system", "content": "Você é somente um assistente que tenta fazer piadas em todos momentos possíveis"}]

def Chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

os.system('cls')
while True:
    pergunta = input("Digite sua pergunta:\nR: ")
    print(Chat(pergunta))