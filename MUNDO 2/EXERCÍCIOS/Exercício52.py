b = 0
a = int(input('Digite o número:'))
for c in range( 1, a+1 ):
   if a % c == 0:
      b += 1
      print('\033[31m', end=' ')
   else:
      print('\033[32m', end=' ')
   print(f'{c}', end=' ')
if b == 2:
    print('\033[m \nÉ primo')
else:
   print('\033[m \nNão é primo')
