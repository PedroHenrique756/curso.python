#Crie um programa que leia o nome completo de uma pessoa e moste: O nome com todas as letras maiúsculas. O nome com todas as letras minúsculas. Quantas letras ao todo (sem considerar os espaços). Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()#aqui ele so vai tirar os espaços do inicio e do final, mas os do meio do nome não
print('Analizando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome contem {} letras'.format(len(nome)-nome.count(' ')))#esse -nome.count(' ') ja vai resolver o probelma dos espaços entre as letras, vale lembra que o que estiver dentro das aspas nesse codigo ira sumir da contagem.