#Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.

nome = str(input('Qual seu nome?:')).title()# aqui ele vai conciderar a primeira letra maiúscula ent nao tera o problema de se o usuario colocar minúsculo e a saida ser falsa.
if 'Silva' in nome:
    print('Ele tem silva no nome')
else:
    print('Ele não tem silva no nome')