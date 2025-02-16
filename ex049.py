#usando o for, faça um programa que pergunte um numero e retorne a tabuada dele.


numero = int(input('Qual o numero que deseja saber a tabuada?: '))

print('\na tabuada do {}'.format(numero))
for somatorio in range(1,11):
    print('{}x{} = {}'.format(numero, somatorio, numero * somatorio))