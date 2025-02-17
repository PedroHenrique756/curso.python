#faça um programa que leia o peso de 5 pessoas e mostre qual foi o maior e o menor entre eles 
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('peso da {}ª pessoa?: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg e o menor peso foi de {}Kg'.format(maior, menor))
