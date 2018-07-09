distancia = int(input('Qual a distância da viagem em km ?: '))
if distancia < 200:
    print('Valor da passagem: {:.2f}'.format(distancia*0.5))
else:
    print('Valor da passagem: {:.2f}'.format(distancia*0.45))

