nomes = []
idades = []
sexos = []
for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))
print('A média de idade é: {}'.format(sum(idades)/4))
for s in sexos:
    if s == 'H':
        