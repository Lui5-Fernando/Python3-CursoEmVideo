import datetime
a = int(input('Digite em que você nasceu:'))
y = datetime.date.today().year
y = y - a
if y > 20:
    print('Master')
elif y >= 19:
    print('Sênior')
elif y >= 14:
    print('Junior')
elif y >= 9:
    print('Infantil')
else:
    print('Mirim')
