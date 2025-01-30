#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('qual o numero?:'))

sucessor = numero +1
antecessor = numero -1

print('o antecessor é {} e o sucessor é {}'.format(antecessor, sucessor))