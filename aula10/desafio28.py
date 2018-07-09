from random import randint
escolhido = int(input('Digite um número: '))
sorteado = randint(0, 5)
if escolhido < 0 or escolhido > 5:
    print('Número inválido, digite um número de 0 a 5')
    exit()
if escolhido == sorteado:
    print('Parabéns você acertou')
else:
    print('Errrrôoou, o número sorteado pelo computador foi: {}'.format(sorteado))