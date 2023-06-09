r1 = float(input('Digite um lado:'))
r2 = float(input('Digite outro lado:'))
r3 = float(input('Digite o último lado:'))
a1 = r1
a2 = r2
maior = r1
if r2>r1 and r2>r3:
    maior = r2
if r3>r1 and r3>r2:
    maior = r3
if (a1 + a2) > maior:
    print('\033[32;40mSim, essas medidas podem formar um triângulo.\033[m')
else:
    print('\033[31mNão, com essas medidas não é possivel vormar um triângulo.\033[m')
