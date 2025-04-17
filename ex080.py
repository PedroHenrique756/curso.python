'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = []

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    
    if len(numeros) == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1

print("\nLista ordenada:")
print(numeros)
