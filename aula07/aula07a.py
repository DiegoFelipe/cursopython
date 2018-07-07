# ORDEM DE PRECEDÊCNIA
# [1] - ()
# [2] - **
# [3] - * / // %
# [4] - + -
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma vale: {}, a multiplação: {}, a divisão: {}, a divisão inteira: {:.3f}, a potência: {}'.format(soma, m, d, di, e))