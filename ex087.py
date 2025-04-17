'''Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                                C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna_3 = 0
maior_valor_linha_2 = 0

# Preenchendo a matriz e já somando valores pares
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

# Calculando a soma da terceira coluna e maior valor da segunda linha
for linha in range(3):
    soma_coluna_3 += matriz[linha][2]

maior_valor_linha_2 = max(matriz[1])

# Exibindo a matriz
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^5} ]", end='')
    print()

# Mostrando os resultados
print(f"\nA) Soma de todos os valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_coluna_3}")
print(f"C) Maior valor da segunda linha: {maior_valor_linha_2}")
