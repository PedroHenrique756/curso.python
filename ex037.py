#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão: -1 para binario -2 para hexadecimal -3 para actal.

num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das opções para base de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXÁDECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXÁDACIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Digite uma opção valida!')