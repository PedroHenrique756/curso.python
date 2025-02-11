#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é o maior, segundo valor é o maior, nao existe valor maior, os dois sao iguais.

num1 = int(input('Qual o primeiro numero?: '))
num2 = int(input('Qual o segundo numero?: '))
if num1 > num2:
    print("O primeiro valor ({}) é maior e o segundo valor ({}) é menor.".format(num1, num2))
elif num2 > num1:
    print("O segundo valor ({}) é maior e o primeiro valor ({}) é menor.".format(num2, num1))
else:
    print("Não existe valor maior, os dois são iguais ({})".format(num1))