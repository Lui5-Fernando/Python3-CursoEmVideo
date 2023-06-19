p = int(input('Digite o primeiro termo de progreção atimédiaca PA:'))
r = int(input('Digite a razão dessa progressão:'))
print(p, end=' = ')
for c in range(0,10):
    p = p+r
    print(p, end=' -> ')
print('Pronto!')
