d = int(input('Digite um número, e lhe mostrarei a tabuada de tal: '))
print ('=' * 20)
print(f'Tabuada de {d}')
print ('=' * 20)
for n in range(1,11):
    s = (n*d)
    print(f'{d} x {n} = {s}')
print ('=' * 20)
