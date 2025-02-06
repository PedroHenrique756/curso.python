#Escreva um programa que que escolha um numero de 0 a 5 e pergunte ao usuario se ele acerta diga que ele venceu se nao diga que ele perdeu.

from random import randint
from time import sleep
pensamento = randint(0, 5)# Faz o computador "PENSAR"
print('\033[33m-=-' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-' * 20)
jogador = int(input('Em qual numero eu pensei?: '))
print('\033[35mPROCESSANDO...')
sleep(3)
if jogador == pensamento:
    print('\033[32mVocê venceu')
else:
    print('\033[31mVocê perdeu, o numero era {}'. format(pensamento))