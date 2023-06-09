n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
if m >= 7:
    print('\33[34mParabéns!!!\033[m \nVocê passou.')
elif m >= 5:
    print('Você está de recuperação:')
else:
    print('\033[31mReprovado.\033[m')