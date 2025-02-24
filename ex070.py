'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

total = totemil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totemil +=1
    
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto 


    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip() .upper()[0]
    if resp == 'N':
        break
print('{:-^40}' .format(' fim do programa '))
print(f'O total da compra foi de R${total}')
print(f'Temos {totemil} produtos acima de R$1000')
print(f'O produto mais foi {barato} custando R${menor} ')
