#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input('qual o seu salario?: '))

aumento = salario * 0.15
nv_salario = aumento + salario 
print('o seu salario será de: {}'.format(nv_salario))