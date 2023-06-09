from datetime import date
a = int(input('Digite um ano qualquer, ou 0 para o ano que estamos\ne descubra se ele é bissexto:'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'\033[32m{a} é um ano bissexto\033[m')
else:
    print(f'\033[31m{a} não é um ano bissexto\033[m.')
