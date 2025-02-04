#faça um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custa R$7 por cada km acima do limite.
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de \033[33mR${:.2f}!'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!')