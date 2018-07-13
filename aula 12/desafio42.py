r1 = int(input('Digite o valor da reta: '))
r2 = int(input('Digite o valor da reta: '))
r3 = int(input('Digite o valor da reta: '))
if (r1 > r2 - r3 and r1 < r2 + r3) and (r2 > r1 - r3 and r2 < r1 + r3) and (r3 > r1 - r2 and r3 < r1 + r2):
    print('Um triângulo pode ser formado')
    if (r1 == r2 == r3):
        print('O triângulo será equilátero')
    elif (r1 == r2 and r2 != r3) or (r1 == r3 and r2 != r3) or (r2 == r3 and r3 != r1):
        print('o triangulo será isóceles')
    else:
        print('o triangulo será escaleno')
else:
    print('Um triângulo NÃO pode ser formado')