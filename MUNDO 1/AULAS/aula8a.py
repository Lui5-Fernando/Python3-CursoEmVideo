import math
n = int(input('Digite um número para descobrir a sua raiz:'))
r = math.sqrt(n)
 # Arredondado para baixo
print(f'A raiz de {n} é {math.floor(r)}')
 # Arredondado para cima
print(f'A raiz de {n} é {math.ceil(r)}')
