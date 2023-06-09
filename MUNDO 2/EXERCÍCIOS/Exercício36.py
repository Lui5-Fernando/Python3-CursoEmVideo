vc = float(input('Digite o valor da casa:R$ '))
p = float(input('Digite quanto você recebe:R$ '))
a = int(input('Digite em quantos anos você pretende pagar essa casa:'))
a = a * 12
'''Quantos mêses vai durar'''
p = (30/100*p)
'''30% do pagamento'''
m = vc/a
'''Valor da mensalidade'''
if m < p:
    print(f'\033[32mVocê pode comprar a casa.\033[m\nSua mensalidade será de {m:.2f} reais mesais')
else:
    print('\033[31mVocê não pode comprar a casa.\033[m')
