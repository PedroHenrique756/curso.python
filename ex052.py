#faça um programa que leia um numero inteiro e diga se ele é um numero primo ou não
num = int(input('Digite um numero: '))
total = 0
for c in range (1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total+= 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[0mO numero {} foi dividido {} vezes'.format(num, total))
if total >= 2:
    print('O seu numero é pirmo.')
else:
    print('O seu numero não é primo.')