'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''

import random

numeros_aleatorios = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", numeros_aleatorios)
print("Menor número:", min(numeros_aleatorios))
print("Maior número:", max(numeros_aleatorios))
