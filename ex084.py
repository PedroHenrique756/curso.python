'''Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                                    A) Quantas pessoas foram cadastradas.                                                                                                                B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.

'''

pessoas = []
maior_peso = menor_peso = 0

while True:
    nome = input("Nome: ").strip()
    peso = float(input("Peso (kg): "))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# A) Total de pessoas
print(f"\nA) {len(pessoas)} pessoas foram cadastradas.")

# B) Pessoas com maior peso
print(f"B) Pessoas com maior peso ({maior_peso} kg): ", end='')
print(', '.join([p[0] for p in pessoas if p[1] == maior_peso]))

# C) Pessoas com menor peso
print(f"C) Pessoas com menor peso ({menor_peso} kg): ", end='')
print(', '.join([p[0] for p in pessoas if p[1] == menor_peso]))
