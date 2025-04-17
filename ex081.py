'''Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = []

while True:
    try:
        valor = int(input("Digite um número (ou digite algo não numérico para sair): "))
        numeros.append(valor)
    except ValueError:
        print("Encerrando entrada de dados...\n")
        break

# A) Quantidade de números digitados
quantidade = len(numeros)

# B) Lista em ordem decrescente
decrescente = sorted(numeros, reverse=True)

# C) Verifica se o número 5 foi digitado
tem_cinco = 5 in numeros

# Resultados
print(f"A) Você digitou {quantidade} números.")
print(f"B) Lista em ordem decrescente: {decrescente}")
print(f"C) O número 5 {'está' if tem_cinco else 'NÃO está'} na lista.")
