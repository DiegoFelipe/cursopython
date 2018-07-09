nome = str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format(nome.lower().__contains__('silva')))
print('Seu nome tem Silva? {} (com operador)'.format('silva' in nome.lower()))
