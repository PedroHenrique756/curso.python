'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''



produtos = (
    "Arroz", 5.50,
    "Feijão", 7.20,
    "Macarrão", 4.30,
    "Leite", 6.80,
    "Pão", 3.50
)

print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<30} R$ {produtos[i+1]:>6.2f}")
print("-" * 40)
