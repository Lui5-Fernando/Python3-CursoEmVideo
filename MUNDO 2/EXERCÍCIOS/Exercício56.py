for nu in range(1,5):
    s = str(input(f'Qual o sexo da {nu}° pessoa (M/F):')).lower()
    if s == 'm':
        n = str(input('Qual o nome desse homem: '))
        ih = int(input('Quantos anos ele tem: '))
        ih += ih
    elif s == 'f':
        n = str(input('Qual o nome dessa mulher: '))
        im = int(input('Quantos anos ela tem: '))
        im += im
    else:
        print('Digite uma opção válida.')
i = ih + im
print(f'A idade média é de:{i/4}')