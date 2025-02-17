#desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 3 primeiros termos dessa progressão 
primeiro = int(input('Primeiro termo: ')) 
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao # enésimo termo de uma PA
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')