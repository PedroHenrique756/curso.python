#crie um programa que leia o nome de uma cidade e diga se começa com o nome 'SANTA'.

cidade = str(input('Qual o nome da sua cidade?')).strip()
print(cidade[:5].title() == 'Santa')