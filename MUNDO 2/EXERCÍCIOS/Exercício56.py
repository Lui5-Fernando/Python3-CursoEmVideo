nn = []
ii = []
ss = []
for nu in range(1,5):
    n = str(input(f'Qual o nome da {nu}° pessoa:'))
    nn.append(n)
    print(nn)
    i = int(input(f'Qual a idade da {nu}° pessoa:'))
    ii.append(i)
    print(ii)
    s = str(input(f'Qual o sexo da {nu}° pessoa (M/F):')).lower()
    if s == 'm' or 'f':
        ss.append(s)
        print(ss)
    else:
        print('Digite uma opção válida:')
