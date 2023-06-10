n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print(f'Sua media foi de {m:.1f}')
if m >= 7:
    print('\33[32mParabéns!!!\033[m \nVocê passou.')
elif m >= 5:
    print('\033[33mVocê está de recuperação:\033[m')
else:
    print('\033[31mReprovado.\033[m')
