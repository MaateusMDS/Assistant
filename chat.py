from app import Chat

import sys
import time
import os

def texto_aparecer(frase):
    for i in frase:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.03)

os.system('cls')

while True:
    pergunta = input("\nDigite sua pergunta... \nR: ")

    resposta = Chat(pergunta)

    print("\n")
    texto_aparecer(resposta + "\n\n")