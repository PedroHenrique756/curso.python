'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
total_maiores = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo [M/F]: ").strip().upper()
    
    if idade > 18:
        total_maiores += 1
    if sexo == "M":
        homens_cadastrados += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if continuar == "N":
        break

print("-" * 30)
print(f"Total de pessoas com mais de 18 anos: {total_maiores}")
print(f"Total de homens cadastrados: {homens_cadastrados}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}")

