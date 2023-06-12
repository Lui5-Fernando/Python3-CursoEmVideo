import time
print('Comtagem regressiva para a queima de fogos:')
for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print('''\033[31mBOM!!
\033[32mBOM!!
\033[33mBOM!!
\033[34mBOM!!
\033[35mBOM!!
\033[36mBOM!!\033[m''')