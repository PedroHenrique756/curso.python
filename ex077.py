''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = (
    "cachorro", "gato", "elefante", "tigre", "leao", "girafa", "hipopotamo"
)

vogais = "aeiou"

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos as vogais:", end=" ")
    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")