num = int(input('Digite um número: '))
total = 0
for c in range(1, num):
    if c != 1 and num % c == 0:
        total += 1
if total >= 2:
    print('não')
else:
    print('sim')

