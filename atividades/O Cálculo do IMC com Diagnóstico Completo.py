alt = float(input('qual a sua altura: '))
peso = float(input('qual o seu peso: '))
imc = peso/(alt * alt)

if imc <= 18.4:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso ideal (parabéns)')
elif imc <= 29.9:
    print('Levemente acima do peso')
elif imc <= 34.9:
    print('Obesidade Grau I')
elif imc > 35.00:
    print('Obesidade Severa/Mórbida')

