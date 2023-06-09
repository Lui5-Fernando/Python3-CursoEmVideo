km = int(input('Que distancia você vai percor em KM? '))
if km <= 200:
    print(f'O valor que você vai pagar é: \033[32m{km * 0.50:.2f} \033[1mreais\033[m')
else:
    print(f'O valor que você vai pagaer é : \033[32m{km * 0.45:.2f} \033[1reais\033[m')
