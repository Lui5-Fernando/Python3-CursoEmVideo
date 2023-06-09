qkm = float(input('Digite quantos kilometros o carro rodou:'))
qd = int(input('Quantos dias o carro ficou alugado:'))
pr = (qkm * 0.15) + (qd * 60)
print (f'Você deve pagar: {pr:.2f} reais.')
