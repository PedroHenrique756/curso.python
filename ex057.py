#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).strip() .upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Invalido!, informe seu sexo novamente [M/F]: ')).strip() .upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))