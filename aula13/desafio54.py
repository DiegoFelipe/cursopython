from datetime import datetime
dimenor = 0
dimaior = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    if datetime.now().year - nascimento >= 21:
        dimaior += 1
    else:
        dimenor += 1
print('Total di menor: {}'.format(dimenor))
print('Total di maior: {}'.format(dimaior))
