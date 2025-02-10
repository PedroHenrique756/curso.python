#crie um programa que leia duas notas de um aluno e qualcule a sua media, mostrando na tela de acordo com a media atingida: media abaixo de 5: reprovado, media entre 5.0 e 5.9 : recuperação, media 7 ou superior: aprovado.

nota1 = float(input('Qual a primeira nota?: '))
nota2 = float(input('Qual a segunda nota?: '))
media_final = (nota1 + nota2) /2
print('Sua media final foi {}'.format(media_final))
if media_final > 7:
    print('Aprovado')
elif media_final < 5:
    print('reprovado')
else:
    print('Recuperação')