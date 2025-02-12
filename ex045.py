#crie um programa que faça o computador jogar jokenpô com você

import random
from time import sleep

print('\033[35m=\033[m'*20)   
print('Vamos jogar jokenpô')
print('\033[35m=\033[m'*20)   

opcoes = ["pedra", "papel", "tesoura"]
jogador = str(input('\033[32mEscolha entre pedra, papel ou tesoura: \033[m')).strip().lower()
computador = opcoes[random.randint(0, 2)]
print('\033[35mProcessando...\033[m')
sleep(3)
print('\033[30mVocê escolheu {}\033[m'.format(jogador))
print('\033[30mO computador escolheu {}\033[m'.format(computador))

#verificando quem ganhou

if computador == jogador:
    print('\033[32mEmpate\033[m')
elif jogador == 'pedra':
    if computador == 'tesoura':
        print('\033[32mVocê venceu\033[m')
    else:
        print('\033[31mVocê perdeu\033[m')
elif jogador == 'tesoura':
    if computador =='papel':
        print('\033[32mVocê venceu\033[m')
    else:
        print('\033[31mVocê perdeu\033[m')
elif jogador == 'papel':
    if computador == 'pedra':
        print('\033[32mVocê venceu\033[m')
    else:
        print('\033[31mVocê perdeu\033[m')
else:
    print('\033[31mEscolha invalida!\033[m')