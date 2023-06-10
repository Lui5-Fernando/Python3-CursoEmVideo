n = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
if n > n2:
    print(f'\033[36m{n} é maior\033[m \n\033[35m{n2} é menor\033[m')
elif n < n2:
    print(f'\033[36m{n2} é maior\033[m \n\033[35m{n} é menor\033[m')
elif n == n2:
    print('\033[32mOs dois são iguais\033[m')
