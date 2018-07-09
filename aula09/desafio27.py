nome = str(input('Digite seu nome completo: ')).strip()
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Ùltimo nome: {}'.format(nome.split()[len(nome.split())-1]))
