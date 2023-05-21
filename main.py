from dotenv import load_dotenv
import openai
import os

load_dotenv()

api_key = os.getenv('API_KEY')

openai.api_key = api_key

messages = [{"role": "system", "content": "Você é um assistente da nike e foi feito somente para indicar produtos de acordo com caracteristicas/gosto indicados. Você só responde assuntos/coisas envolvendo a nike, fora disso, você não responde."}]

def Chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply