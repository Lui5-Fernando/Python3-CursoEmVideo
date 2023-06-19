
b = 0
c = 999999999
for a in range(1,6):
    p=float(input(f'Digite o peso da {a}° pesssoa:'))
    if p > b:
        b = p
    elif p < c:
        c = p
print(f'O maior foi: {b:.1f}')
print(f'O menor foi: {c:.1f}')