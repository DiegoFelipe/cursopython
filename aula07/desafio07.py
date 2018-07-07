altura = float(input('Digite a altura da parede'))
largura = float(input('Digite a largura da parede'))
area = altura * largura
print('Para pintar a parede você precisará de {:.0f} litros de tinta'.format(area/2))
