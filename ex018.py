#faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo

import math 

an = float(input('Qual o ângulo você deseja: '))
sn = math.sin(math.radians(an))
print('O ângulo {} tem o SENO de {:.2f}'.format(an, sn))
cs = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cs))
tn = math.tan(math.radians(an))
print('O ângulo de {} tem sua TANGENTE de {:.2f}'.format(an, tn))
