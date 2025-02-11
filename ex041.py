"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date
ano = int(input('Qual o ano que você nasceu?: '))
ano_atual = date.today().year
idade =  ano_atual - ano
if idade < 9:
    print('Ele é um atleta MIRIM')
elif idade < 14:
    print('Ele é um atleta INFANTIL')
elif idade < 19:
    print('Ele é um atleta JÚNIOR')
elif idade < 20:
    print('Ele é um atleta SÊNIOR')
else:
    print('Ele é MESTRE')
