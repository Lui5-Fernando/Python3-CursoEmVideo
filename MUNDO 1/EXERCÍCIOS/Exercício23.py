nu = int(input('Digite o número:'))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print(f'Esse número tem {u} undade(s)')
print(f'Esse número tem {d} desena(s)')
print(f'Esse número tem {c} centena(s)')
print(f'Esse número tem {m} milhar(es)')
nu = str(input('Digite o número:'))
print('undide(s)',nu[3])
print('desena(s)',nu[2])
print('centena(s)',nu[1])
print('milhar(es)',nu[0])
