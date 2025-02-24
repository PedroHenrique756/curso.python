#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

vitorias = 0

while True:
    jogador_escolha = input("Par ou Ímpar? ").strip().lower()
    jogador_numero = int(input("Escolha um número: "))
    computador_numero = random.randint(0, 10)
    soma = jogador_numero + computador_numero
    
    print(f"Você escolheu {jogador_escolha} e jogou {jogador_numero}")
    print(f"O computador jogou {computador_numero}")
    print(f"Soma: {soma}")
    
    resultado = "par" if soma % 2 == 0 else "ímpar"
    
    if resultado == jogador_escolha:
        print("Você venceu!")
        vitorias += 1
    else:
        print("Você perdeu!")
        break

print(f"Fim do jogo! Você conseguiu {vitorias} vitória(s) consecutiva(s).")
