'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = input("Digite uma expressão com parênteses: ")
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            # Encontrou um ')' sem um '(' correspondente
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Expressão válida! Os parênteses estão corretos.")
else:
    print("Expressão inválida! Os parênteses estão incorretos.")
