#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.


n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

a, b = 0, 1
print("Sequência de Fibonacci:", end=" ")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()