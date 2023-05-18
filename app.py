from flask import Flask, request
from main import Chat
import json

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def get_data():
    data = request.data
    json_data = request.get_json()

    resposta = json_data["mensagem"]

    resposta = Chat(resposta)

    return resposta

    

    # answer = Chat(json_data)

    # return answer

if __name__ == '__main__':
    app.run()