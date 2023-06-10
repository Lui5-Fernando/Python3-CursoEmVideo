import time
import random
print('-=-' * 7)
print('Escolha uma da opções:')
print('-=-' * 7)
print('-=-' * 4)
print('|[1]Pedra  |')
print('|[2]Papel  |')
print('|[3]Tesolra|')
print('-=-' * 4)
op = int(input('Digite a opção da jogada:'))
time.sleep(0.5)
print('PEDRA')
time.sleep(0.5)
print('PAPEL')
time.sleep(0.5)
print('TESOLRA!!!')
print('-=-' * 5)
pc = random.randint(1,3)
if op == pc:
    print('Empate')
elif op == 1 and pc == 2:
    print('Você: Pedra \nPC: Papel \n\033[31mVocê Perdeu!\033[m')
elif op == 1 and pc == 3:
    print('Você: Pedra \nPC: Tesolra \n\033[32mVocê Ganhou!\033[m')
elif op == 2 and pc == 1:
    print('Você: Papel \nPC: Pedra \n\033[32mVocê Ganhou!\033[m')
elif op == 2 and pc == 3:
    print('Você: Papel \nPC: Tesolra \n\033[31mVocê Perdeu!\033[m')
elif op == 3 and pc == 1:
    print('Você: Tesolra \nPC: Pedra \n\033[31mVocê Perdeu!\033[m')
elif op == 3 and pc == 2:
    print('Você: Tesolra \nPC: Papel \n\033[32mVocê Ganhou!\033[m')
else:
    print('Algo deu errado!!!')
 