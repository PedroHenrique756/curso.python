'''
faça um programa que leia nome, idade e sexo de 4 pessoas. No final o programa mostra:
-A media de idade do grupo 
-qual o nome do home mais velho 
-quantas mulhes tem menos de 20 anos
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int (input ('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('A idade do home mais velho é {} anos e ele se chama {}'.format(maioridadehomem, homemvelho))
print('A quantidade de mulheres que tem menos de vinte anos é de {}'.format(totmulher20))
