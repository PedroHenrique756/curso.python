#melhore o desafio 61, pergunte ao usuario se ele quer mostrar mais algum termo, o programa encerra quando ele disse que quer mostrar 0 termo.

primeiro = int(input('Primeiro termo: ')) 
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total+=mais
    while cont <= 10:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont +=1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM.')