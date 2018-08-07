
escolha = 0
while escolha != 5:
    num = int(input('Digite o primeiro número'))
    num2 = int(input('Digite o segundo número'))
    print('selecione a operação \n')
    print('[1] somar')
    print('[2] multiplar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair')
    escolha = int(input())
    if(escolha < 0 or escolha > 5):
        print('Operação inválida!')
    elif escolha == 5:
        break;
    elif escolha == 1:
        print('A soma de {} e {} é = {}'.format(num, num2, num+num2))
    elif escolha == 2:
        print('{} x {} = {}'.format(num, num2, num * num2))
    elif escolha == 3:
        print('O maior número é {}'.format(max(num,num2)))

