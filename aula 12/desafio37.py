num = int(input('Digite um número: '))
print('Digite 1 para base binária')
print('Digite 2 para base octal')
print('Digite 3 para base hexadecimal')
conv = int(input('Escolha a base para conversão:'))
if conv == 1:
    print('{} em base binária: {}'.format(num, bin(num)[2:]))
if conv == 2:
    print('{} em base octal {}'.format(num, oct(num)))
if conv == 3:
    print('{} em base hexadecimal: {}'.format(num, hex(num)))
