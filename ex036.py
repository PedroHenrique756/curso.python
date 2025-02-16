#escreva um programa aprovar o emprestimo bancario para a compra de uma casa. O programa vai pergunta o VALOR DA CASA, o SALARIO do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele nao pode excender 30% do salario ou então o emprestimo será negado. 

valor_casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o seu salario?: R$'))
parcela = int(input('Qualtas vezes vc quer parcelar?: '))
prestação = valor_casa / (parcelas *12)
minimo = salario *30 / 100
print('Para pagar uma casa de R${:.2f} e {} anos, á prestação será de R${:.2f}'.format(valor_casa, parcela, prestação))
if prestação <=minimo:
    print('Emprestimo pode ser consedido')
else:
    print('Emprestimo negado')