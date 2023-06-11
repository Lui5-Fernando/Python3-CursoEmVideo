a = 0
for n in range(1,7):
    v = int(input(f'{n}º número: '))
    if v % 2 == 0:
        a = a + v
print(f'A soma dos números pares digitados foi de {a} .')
