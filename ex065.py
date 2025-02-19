#crie um programa que leia varios numeros inteiro pelo teclado , no final, mostre a media entre todos eles, qual foi o maior e qual foi o menor, pergunte se o usuario ainda quer continuar a digitar os valores.
soma = 0
cont = 0 

while int:
    numero = int(input('Qual o numero?: '))
    parada = str(input('Deseja continuar? [S/N]: ')).upper()
    if parada == 'N':
        break
    else:
        soma += numero
        cont += 1

media = soma / cont
print('A soma de todos os numeros é de {}'.format(soma))
print('A media entre ele é de {}'.format(media))