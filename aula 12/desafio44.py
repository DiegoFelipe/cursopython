preco_normal = float(input('Digite o preço normal: '))
print('1 - á vista (dinheiro/cheque)')
print('2 - á vista no cartão')
print('3 - até 2x no cartão')
print('4 - 3x ou mais no cartão')
condicao = int(input('Escola a condição: '))

if condicao == 1:
    total = preco_normal - (preco_normal/100)* 10
elif condicao == 2:
    total = preco_normal - (preco_normal/100) * 5
elif condicao == 3:
    total = preco_normal
else:
    total = preco_normal + (preco_normal/100) * 20

print('total a pagar: {}'.format(total))
