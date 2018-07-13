num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2 or num2 > num1:
    print('O maior número é {}'.format(num1 if num1 > num2 else num2))
if num1 == num2:
    print('Os dois número são iguais')
