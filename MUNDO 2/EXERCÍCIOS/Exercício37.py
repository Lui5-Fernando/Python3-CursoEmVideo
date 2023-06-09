n = int(input('Digite um número:'))
print('-=-'* 5 + '=')
print('|[1]Binário    |')
print('|[2]Octal      |')
print('|[3]Hexadecimal|')
print('-=-'* 5 + '=')
op = int(input('Escolha uma opção de coverção:'))
if op == 1:
    print(f'Binário: {bin(n)[2:]}')
elif op == 2:
    print(f'Octal: {oct(n)[2:]}')
elif op == 3:
    print(f'Hexadecima {hex(n)[2:]}')
else:
    print('Opção inválida.')
