n = int(input('Digite um número para saber se ele é par ou impar:'))
if n % 2 == 0:
    print('\033[44mPar\033[m')
else:
    print('\033[45mImpar\033[m')