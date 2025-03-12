'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times_brasileirao = (
    "Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo",
    "Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG",
    "Botafogo", "Santos", "Goiás", "Bragantino", "Coritiba",
    "Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Chapecoense"
)

print("Os 5 primeiros times são:", times_brasileirao[:5])
print("\nOs últimos 4 colocados são:", times_brasileirao[-4:])
print("\nTimes em ordem alfabética:", sorted(times_brasileirao))

if "Chapecoense" in times_brasileirao:
    print(f"\nA Chapecoense está na posição {times_brasileirao.index('Chapecoense') + 1}.")
else:
    print("\nA Chapecoense não está entre os 20 primeiros.")