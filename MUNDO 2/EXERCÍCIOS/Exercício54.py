import datetime
ma = 0
me = 0
ano = datetime.date.today().year
for a in range(1,8):
    i = int(input(f'Qual o ano de nascimentro da {a}° pessoa:'))
    an = ano - i
    if an >= 21:
        ma = ma + 1
    else:
        me = me + 1
print(f'A quantidade de maiores é {ma}.')
print(f'A quantidade de menores é {me}.')
