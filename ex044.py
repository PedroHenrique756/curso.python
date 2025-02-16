preco = float(input('Qual o preço das compras?: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no catão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif preco == 2:
    total = preco - (preco *5 / 100)
elif preco == 3:
    total = preco
    parcela = total / 2
    print('sua compra sera parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 /100)
    total_parcelas = int(input('Quantas parcelas são?: '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas , parcela))
else:
    total = preco
    print('INVALIDO. tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))