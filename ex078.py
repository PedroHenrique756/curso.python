'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições'''

valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um numero da posição {cont}: ')))

if valores:
    maior = max(valores)
    ps_maior = valores.index(maior)

    menor = min(valores)
    ps_menor = valores.index(menor)

print(f'o maior numero deles é: {maior} nas posições: {ps_maior}')
print(f'o menor deles é: {menor} nas posições: {ps_menor}')


