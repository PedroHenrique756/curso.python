#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se ja passou do tempo de se alistar. Seu programa também deverá mostra o tempo que falta ou que passou do prazo.

from datetime import date

#ano atual
ano_atual = date.today().year

# Solicitando o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calculando a idade
idade = ano_atual - ano_nascimento

# Definindo a idade para o alistamento obrigatório
idade_alistamento = 18

diferenca = idade - idade_alistamento

# Verificando a situação do alistamento
if idade < idade_alistamento:
    print("Você ainda vai se alistar ao serviço militar. Faltam {} anos.".format(abs(diferenca)))
elif idade == idade_alistamento:
    print("É a hora de se alistar ao serviço militar!")
else:
    print("Você já passou do tempo de alistamento. Já se passaram {} anos.".format(diferenca))
