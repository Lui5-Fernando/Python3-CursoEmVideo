a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
c = int(input('Digite o último número:'))
me = a
ma = a
if b<a and b<c:
    me = b
if c<a and c<b:
    me = c
if b>c and b>a:
    ma = b
if c>a and c>b:
    ma = c
print(f'O menor número é {me}.')
print(f'O maior número é {ma}.')