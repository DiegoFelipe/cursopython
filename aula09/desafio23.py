num = input('Digite um número de 0 a 9999')
numint = int(num)
tam = len(num)
if numint >= 0 and numint <= 9999:
    if len(num) == 4:
        print('Milhar: {}'.format(num[tam-4]))
    if len(num) >= 3:
        print('Centenas: {}'.format(num[tam-3]))
    if len(num) >= 2:
        print('Dezenas: {}'.format(num[tam-2]))
    if len(num) >= 1:
        print('Unidades: {}'.format(num[tam-1]))
else:
    print('Número inválido, digite entre 0 e 9999')
