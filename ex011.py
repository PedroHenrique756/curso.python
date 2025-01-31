# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.

largura = float (input('qual a largura da parede em metros?:'))
altura = float (input('qual a altura em metros da parede?'))

area = largura * altura / 2

print('a quantidade de tinta que precisa é {}'.format(area))

