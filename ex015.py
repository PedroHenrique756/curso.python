#escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos quais foram alugados. Calcule p preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km = float (input('quantos KMs voce rodou?:'))
dias = int (input ('quantos dias voce ficou com o carro?'))

dia = dias * 60 
km = km * 0.15 
total = dia + km

print('O valor pelo dia fica: {}, pelo KM fica: {}, e o total fica: {}'. format(dia, km, total))