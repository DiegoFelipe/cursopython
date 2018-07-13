from random import randint
print('JOKENPÔ')
print('Escolha uma das opções: ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
names = ['Pedra', 'Papel', 'Tesoura']
escolhido = int(input(''))
sorteado = randint(1, 3)
if escolhido == sorteado:
    print('empate!')
elif (escolhido == 1 and sorteado == 3) or (escolhido == 2 and sorteado == 3 ) or (escolhido == 3 and sorteado == 2):
    print('você ganhou! o computador escolheu: {}'.format(names[sorteado-1]))
else:
    print('você perdeu! o computador escolheu: {}'.format(names[sorteado-1]))


