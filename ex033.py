#faça um program que leia três numeros e mostre qual é o maior e o menor deles.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Seugundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3 
if n1>n2 and n1>3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))