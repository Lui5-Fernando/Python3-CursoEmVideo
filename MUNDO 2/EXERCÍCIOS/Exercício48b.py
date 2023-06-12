c = 0
d = 0
for n in range(1,500):
    if n % 3 == 0:
        a = n
        if a % 2 != 0:
            b = a
            c += b
            d += 1
            print(b)
print(f'O total da soma dos {d} números foi \033[32m{c}\033[m .')
