#crie um program que leia varios numeros inteiros pelo teclado, o programa so vai parar quando o usuario digitar 999,condição de parada. No final, mostre quantos numeros foram digitados e e qual foi a soma entre eles desconsiderando o flag

soma = 0
cont = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f"A quantidade de numeros digitados foi de {cont}")
print(f'A soma entre todos eles foi de {soma}')