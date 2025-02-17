#desenvolva um program que leia 6 numeros e retorne a soma dos numeros, mas somente os pares desconsiderando os imparis
soma = 0
for c in range(1, 7):
    num = int(input('Qual o {} valor'.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma de 6 numeros e a soma foi {}'.format(soma))
