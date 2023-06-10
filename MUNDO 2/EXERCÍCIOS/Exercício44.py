p = float(input('Digite o valor das compras: R$'))
print('Escolha a opção de pagamento:')
print('-=-' * 13)
print('|[1]A vista : 10% de desconto          |')
print('|[2]A vista no cartão : 5% de desconto |')
print('|[3]2X no cartão                       |')
print('|[4]3X ou mais no cartão : 20% de juros|')
print('-=-' * 13)
op = int(input('Digite a opção q melhor lhe agrada: '))
if op == 1:
    print(f'O valor total é:{p-(10/100*p)}')
elif op == 2:
    print(f'O valor total é:{p-(5/100*p)}')
elif op == 3:
    print(f'O valor total é:{p }')
elif op == 4:
    print(f'O valor total é:{(20/100*p)+p } reais')
else:
    print('Opção inváida.')
