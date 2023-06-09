'''b = float(input('Digite:'))
c = float(input('Digite:'))
a2 = ((b**2) + (c**2))** (1/2)
print(f'a hipotenusa é {a2:.2f}')'''
import math
b = float(input('Digite:'))
c = float(input('Digite:'))
a = math.hypot(b,c)
print(f'a hipotenusa é {a:.2f}')
