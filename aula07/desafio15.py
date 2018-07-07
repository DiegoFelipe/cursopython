dias = int(input('Quantos dias? '))
km = float(input('Quantos KM percorridos?'))
preco = 60*dias+km*0.15
print('total a pagar: R${:.2f}'.format(preco))
