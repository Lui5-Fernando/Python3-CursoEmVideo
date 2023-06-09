km = int(input('Digite a sua velocidade em KM/h:'))
if km > 80:
    m = (km - 80) * 7
    print(f' \033[1;31mVocê está acima do limte permitido \n Você foi multado em \033[41m{m:.2f}\033[m\033[31m reais.\033[m')
else:
    print('\033[1;32mPrabéns, você está dentro do limite permitido\033[m')
