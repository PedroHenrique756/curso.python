#crie um porgrama que leia o ano de  nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maior idade e quantas ja sao maiores ( 21anos )
ano_atual = 2025
maior = 0
menor = 0
for i in range(7):
    ano = int(input('Qual a data do seu aniversario?'))
    idade = ano_atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Temos {} que são de maior idade'.format(maior))
print('Temos {} que são de menor idade'.format(menor))