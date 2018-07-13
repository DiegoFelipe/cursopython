from datetime import  datetime
ano = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - ano
if idade <= 9:
    print('Categoria: Mirim')
if idade <= 14:
    print('Categoria: Infatil')
if idade <= 19:
    print('Categoria: Júnior')
if idade > 19:
    print('Categoria: Master')