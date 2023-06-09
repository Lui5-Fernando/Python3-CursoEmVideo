n1 = int(input('Digite o primeiro ângulo:'))
n2 = int(input('Digite o segundo ângulo:'))
n3 = int(input('Digite o terceiro ângulo:'))
if n1 + n2 > n3 or n2 + n3 < n1 or n1 + n3 < n2:
    if n1 == n2 and n2 == n3:
        print('Esse é um triângulo equilátero')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Esse é triângulo isósceles')
    else:
        print('Esse é um triâgulo escaleno')
else:
    print('Com esses ângulos não é possivel formar um triângulo.')