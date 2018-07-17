import datetime
ano = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - ano
if idade < 17:
    print('ainda vai ter que se alistar')
elif idade   > 17 and idade < 19:
    print('está na hora de se alistar')
else:
    print('já passou da hora de se alistar')
