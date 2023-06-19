a = str(input('Digite a frase e verifique se ela é um políndromo:')).lower()
b = ''.join(a[::-1].split())
c = ''.join(a.split())
if b == c:
    print('\033[32mEssa frase é um políndromo\033[m')
else:
    print('\033[31mEssa frase não é um políndromo\033[m')
