'''
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
sleep(1)
while opcao != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicação))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
             maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida')
    print('-=-'*10)
    sleep(1)
print('Fim do programa.')
