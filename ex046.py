#faça um programa que que mostre na tela uma contagem regressiva para o estouro de folgos de artificio, ido de 10 a 0, com uma pausa de um segundo entre eles
from time import sleep

for c in range(1, 11):
    print(c)
    sleep(1)
print('fim')