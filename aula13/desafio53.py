frase = str(input('Digite uma frase')).strip()
if frase == frase[::-1]:
    print('é um palíndromo')
else:
    print('Não é um palíndromo')
