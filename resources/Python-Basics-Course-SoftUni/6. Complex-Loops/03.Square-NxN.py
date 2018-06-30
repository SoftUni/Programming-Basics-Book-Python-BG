# Квадрат от звездички

n = int(input())
for row in range(1, n + 1):
    print('*', end='')
    for col in range(1, n):
        print(' *', end='')
    print()