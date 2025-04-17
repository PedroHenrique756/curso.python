'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numeros = []

while True:
    try:
        valor = int(input("Digite um número (ou digite 'sair' para encerrar): "))
        if valor not in numeros:
            numeros.append(valor)
        else:
            print("Número duplicado! Não será adicionado.")
    except ValueError:
        opcao = input("Deseja encerrar? (s/n): ").strip().lower()
        if opcao == 's':
            break

# Ordena os valores únicos em ordem crescente
numeros.sort()

print("\nNúmeros digitados (sem repetições), em ordem crescente:")
print(numeros)
