nota1 = int(input('Digite a nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = float((nota1 + nota2) / 2)

if media < 5:
    print('reprovado')
elif media >= 5 and media <= 6.9:
    print('recuperação')
else:
    print('aprovado')
