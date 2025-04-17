''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

todos = []
pares = []
impares = []

while True:
    try:
        valor = int(input("Digite um número (ou digite algo não numérico para sair): "))
        todos.append(valor)

        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    except ValueError:
        print("\nEntrada encerrada!\n")
        break

print(f"Todos os valores digitados: {todos}")
print(f"Valores pares: {pares}")
print(f"Valores ímpares: {impares}")
