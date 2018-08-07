from random import randint

tentativas = escolhido = 0
sorteado = 1
while escolhido != sorteado:
    escolhido = int(input('Digite um número: '))
    sorteado = randint(0, 10)
    if escolhido < 0 or escolhido > 10:
        print('Número inválido, digite um número de 0 a 5')
    elif escolhido == sorteado:
        print('Parabéns você acertou')
    else:
        print('Errrrôoou, o número sorteado pelo computador foi: {}'.format(sorteado))
    tentativas += 1
print("Você tentou {} vezes para acertar".format(tentativas))