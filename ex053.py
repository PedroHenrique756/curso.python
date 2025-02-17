#faça um programa que leia uma frase qualquer e retorne se ela é ou nao um palindromo, desconsiderando os espaços.
frase = str(input('Qual a frase?: ')).strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Sua plavra não é um palindromo ')
