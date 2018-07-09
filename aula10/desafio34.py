salario = int(input('Digite o salário: '))
if salario >= 1250:
    print('O aumento é de: {:.2f}'.format((salario/100)*15))
else:
    print('O aumento é de: {:.2f}'.format((salario/100)*10))
