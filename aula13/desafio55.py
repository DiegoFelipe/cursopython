pesos = []
for c in range(0, 5):
    peso = float(input('Digite o peso da {}a pessoa: '.format(c+1)))
    pesos.append(peso)
print('O maior peso é: {}'.format(max(pesos)))
print('O menor peso é: {}'.format(min(pesos)))
