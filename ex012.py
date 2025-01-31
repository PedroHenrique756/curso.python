#faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('qual o preço do produto?'))

desconto = preço * 0.05
novo_preço = preço - desconto

print('o desconto fica de {} e o preço do produto fica: {}'. format(desconto,  novo_preço))