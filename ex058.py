#Melhore o jogo do desafio 28 onde o computador vai pesar em um numero entre 0 a 10, so que agora o jogador vai jogar ate adivinhar, mostrando no final quantos palpites foram necessário para vencer.

from random import randint
from time import sleep

cont = 0
pensamento = randint(0, 10)
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
jogador = int(input('Em qual numero eu pensei?: '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
while jogador != pensamento:
    cont+= 1
    jogador = int(input('\033[31mVocê errou!\033[m, tente novamente, Em qual numero eu pensei?: '))
print('\033[32mVocê venceu!\033[m')
print('Você precisou de {} tentativas para ganhar'.format(cont))
