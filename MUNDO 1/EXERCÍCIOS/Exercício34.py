s = float(input('Qual o seu salario? R$'))
if s > 1250 :
    print(f'Seu novo salario com o almento de \033[1m10%\033[m é:\033[32m{(10/100)* s + s:.2f}\033[m reais.')
else:
    print(f'Seu novo salario com o almento de \033[1m15%\033[m é:\33[32m{((15/100)* s) + s:.2f}\033[m reais.')
