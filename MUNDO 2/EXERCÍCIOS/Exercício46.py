import time
print('Comtagem regressiva para a queima de fogos:')
for c in range(11,0,-1):
    time.sleep(0.5)
    print(c-1)
print('''\033[31mBOM!!
\033[32mBOM!!
\033[33mBOM!!
\033[34mBOM!!
\033[35mBOM!!
\033[36mBOM!!\033[m''')