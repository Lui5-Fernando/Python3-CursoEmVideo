d = int(input('Digite um número, e lhe mostrarei a tabuada de tal: '))
print ('=' * 20)
print(f'Tabuada de {d}')
print ('=' * 20)
for n in range(0,10):
    s = (n*d)+d
    print(f'{n+1} x {d} = {s}')
print ('=' * 20)
