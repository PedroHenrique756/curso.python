#Escreva um programa que leia um valor em metros e o exiba convertido para centímetros a milímetros

metros = float (input('digite o valor em metros:'))

centimetros = metros * 100
milimetros = metros *1000
print('o valor em metros de {} em cm é {} e em milimetros é {}'.format(metros, centimetros, milimetros ))