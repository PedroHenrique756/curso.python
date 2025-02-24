#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('-=-' *10)
print('TABUADA')
print('-=-' *10)
while True:
    numero = int(input('Digite um numero (negativo para parar): '))

    if numero < 0:
        print('programa finalizado')
        break

    print(f'A tabuada de {numero} é')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('-=-' *20)
    print('NOVAMENTE')
    print('-=-' *20)