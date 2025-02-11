peso = float(input('Qual o seu peso (kg)?: '))
altura = float(input('Qual a sua altura (m)?: '))

imc = peso / (altura ** 2)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('\033[31mVocê está abaixo do peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[33mVocê está com sobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[31mVocê está com obesidade!\033[m')
else:
    print('\033[41mVocê está com obesidade mórbida!\033[m')
