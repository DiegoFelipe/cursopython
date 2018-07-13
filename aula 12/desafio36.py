valor_casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o salário: '))
anos = int(input('em quantos anos vai ser paga?: '))

valor_parcela = valor_casa / (anos * 12)
if (valor_parcela > (salario/100*30)):
    print('Empréstimo Negado, pois o valor da parcela é {:.2f}'.format(valor_parcela))
else:
    print('Empréstimo aprovado')