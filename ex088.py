'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

'''

import random
from time import sleep

print("-" * 40)
print("     GERADOR DE PALPITES DA MEGA SENA     ")
print("-" * 40)

jogos = []
quantidade = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(quantidade):
    jogo = sorted(random.sample(range(1, 61), 6))  # Sorteia 6 números únicos e ordena
    jogos.append(jogo)

print("\nSORTEANDO OS JOGOS...\n")
for i, jogo in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jogo}")
    sleep(0.5)  # Pequena pausa para dar suspense

print("\nBoa sorte!")
