#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex:. digite um numero: 6.127 tem a parte inteira 6.
import math

num = float(input('qual o numero Real?:'))
print('A parte inteira do numero {} é {}'.format(num, math.trunc(num)))