from random import randint, shuffle

alunos = ['Gustavo', 'Pedrinho', 'Paty', 'Mariazinha']
escolhidos = []
nomeEscolhidos = []
while len(nomeEscolhidos) < 4:
    jaUsado = False
    ordem = randint(0, 3)
    for e in escolhidos:
        if e == ordem:
            jaUsado = True
    if jaUsado == False:
        escolhidos.append(ordem)
        nomeEscolhidos.append(alunos[ordem])
print('Ordem dos alunos escolhidos: {} {} {} {}'.format(nomeEscolhidos[0], nomeEscolhidos[1], nomeEscolhidos[2], nomeEscolhidos[3]))
print('Escolhidos automaticamente:')
shuffle(alunos)
print(alunos)



