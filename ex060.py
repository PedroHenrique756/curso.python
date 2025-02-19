'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

'''

from math import factorial

num = int(input('Digite um numero para calcular o seu fatorial'))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))