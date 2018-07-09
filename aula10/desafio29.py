velocidade = int(input('Digite a velocidade do carro: '))
if velocidade < 0:
    print('Velocidade inválida')
    exit()
if velocidade > 80:
    print('Você ultrapassou a velocidade permitida, valor da multa: R${:.2f}'.format((velocidade-80)*10))
else:
    print('Você está dentro do limite')
