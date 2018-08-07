num = int(input('Digite um numero'))
prox = 0
fat = num
while (num >= 1):
    if (prox == 0):
        fat = num * (num-1)
    else:
        fat += (num - 1)
    num -= 1
    prox += 1
print('O fatorial é {}'.format(fat))