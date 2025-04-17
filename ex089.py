'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

# Lista para armazenar os dados dos alunos
alunos = []

# Função para ler os dados dos alunos
while True:
    nome = input("Digite o nome do aluno: ").strip()
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    
    # Calculando a média
    media = (nota1 + nota2) / 2
    
    # Adicionando os dados na lista composta
    alunos.append([nome, [nota1, nota2], media])
    
    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro aluno? (S/N): ").strip().upper()
    if continuar == 'N':
        break

# Exibindo o boletim com a média de cada aluno
print("\nBOLETIM FINAL:")
for aluno in alunos:
    print(f"{aluno[0]}: Média = {aluno[2]:.2f}")

# Perguntando se o usuário quer ver as notas de algum aluno
while True:
    nome_busca = input("\nDigite o nome do aluno para ver as notas (ou 'Sair' para encerrar): ").strip()
    
    if nome_busca.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    encontrado = False
    for aluno in alunos:
        if aluno[0].lower() == nome_busca.lower():
            print(f"As notas de {aluno[0]} são: {aluno[1][0]} e {aluno[1][1]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Aluno não encontrado!")
