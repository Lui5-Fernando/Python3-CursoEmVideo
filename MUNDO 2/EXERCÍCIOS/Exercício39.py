import datetime
a = int(input('Digite em que ano você nasceu:'))
at = datetime.date.today().year
a = at - a
at = a - 18
if a < 18:
    if at == -1:
        print(f'Você ainda não precisa se alistar, falta {-(at)} ano.')
    else:
        print(f'Você ainda não precisa se alistar, faltam {-(at)} anos.')
elif a > 18:
    if at == 1:
        print(f'Já se passou {at} ano da hora de se alistar .')
    else:
        print(f'Já se passou {at} anos da hora de se alistar .')
elif a == 18:
    print('Você deve se alistar.')
