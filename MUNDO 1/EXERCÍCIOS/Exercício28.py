from random import randint
from time import sleep
print('-=-'* 19)
a = int(input('\033[36mDigite um número de 0 a 5, e veja se eu pensei o mesmo:\033[m'))
print('-=-' * 19)
r = randint(0,5)
print(f'CARREGANDO...\n','-=-' * 4)
sleep(1)
if a == r:
    print(f'\033[32mTambém pensei em {r}.\033[m')
else:
    print(f'\033[31mEu pensei em {r}, diferente de você que pensou em {a}.\033[m')
