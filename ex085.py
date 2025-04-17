'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = [[], []]  # números[0] = pares, números[1] = ímpares

for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

# Ordenando as duas listas
numeros[0].sort()
numeros[1].sort()

print("\nValores pares em ordem crescente:", numeros[0])
print("Valores ímpares em ordem crescente:", numeros[1])
