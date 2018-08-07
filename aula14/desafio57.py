sexo = 'v'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print("digite m ou f ")
