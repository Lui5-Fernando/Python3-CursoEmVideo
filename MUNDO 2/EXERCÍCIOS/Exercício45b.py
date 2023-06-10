import random
import time
it = ('','Pedra', 'Papel', 'Tesolra')
pc = random.randint(1, 3)
'''O primeiro item de uma lista vale 0'''
print('-=-' * 7)
print('Escolha uma da opções:')
print('-=-' * 7)
print('-=-' * 4)
print('\033[36m|[1]Pedra  |')
print('|[2]Papel  |')
print('|[3]Tesolra|\033[m')
print('-=-' * 4)
op = int(input('Digite a opção da jogada:'))
time.sleep(0.5)
print('-=-' * 5)
print('PEDRA')
time.sleep(0.5)
print('PAPEL')
time.sleep(0.5)
print('TESOLRA!!!')
print('-=-' * 5)
if op == 1 or op == 2 or op == 3:
    print('-=-' * 8)
    print(f'\033[35mO pc escolheu {it[pc]}')
    print(f'O player escolheu {it[op]}\033[m')
    print('-=-' * 8)
    if pc == op:
        print('\033[33mEmpate!\033[m')
    elif (pc == 1 and op == 3) or (pc == 2 and op == 1) or (pc == 3 and op == 2):
        print('\033[31mVocê Perdeu!\033[m')
    else:
        print('\033[32mVocê Ganhou!\033[m')
else:
    print('\033[31mAlgo deu errado!!!\033[m')
