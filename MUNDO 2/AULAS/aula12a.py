import datetime
print('Escolha uma cor:')
print("-=-" * 5)
print('[1] Azul')
print('[2] Verde')
print('[3] Vermelho')
print("-=-" * 5)
f = int(input('Número da cor:'))
if f == 1:
    print('\033[30;44mAzul\033[m')
else:
    if f == 2:
        print('\033[30;42mVerde\033[m')
    else:
        if f == 3:
            print('\033[30;41mVermelho\033[m')
        else:
            print('Opção iválida.')

