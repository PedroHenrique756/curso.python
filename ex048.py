#faça um programa que calcule a soma entre todos os numero impares que são multiplos de três e que se encontra no intervalo de 1 até 500
soma = 0 #acumulador 
cont = 0 #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont +=  1
        soma += c
print('A soma de todos os {} valores slolicitados é {}'.format(cont, soma))