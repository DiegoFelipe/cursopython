peso = float(input('digite o peso: '))
altura = float(input('digite a altura: '))
imc = peso / (altura*altura)
if imc <= 18.5:
    print('abaixo do peso')
elif imc > 18.8 and imc <= 25:
    print('peso ideal')
elif imc > 25 and imc <= 30:
    print('sobrepeso')
else:
    print('obesidade mórbida')
