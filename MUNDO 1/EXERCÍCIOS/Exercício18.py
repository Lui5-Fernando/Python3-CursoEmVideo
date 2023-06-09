import math
an = int(input('Digite o ângulo:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O ângulo \033[31m{an}\033[m tem o seno \033[32m{sen:.2f}\033[m o cosseno \033[33m{cos:.2f}\033[m tangente \033[34m{tan:.2f}\033[m')
