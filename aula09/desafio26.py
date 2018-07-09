frase = str(input('Digite uma frase: ')).strip().upper()
checkA = 'A' in frase.upper()
if(frase == ''):
    print('sua frase está vazia')
    exit()
if(checkA == False):
    print('Sua frase não tem a letra A')
    exit()
else:
    print('A letra A aparece {} vezes'.format(frase.count('A')))
    print('A primeira ocorrência da letra A é em {}'.format(frase.find('A')+1))
    print('A última letra A apareceu na posição: {}'.format(frase.rfind('A')+1))
