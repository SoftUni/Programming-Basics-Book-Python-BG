# Триъгълник от долари

n = int(input())
for row in range(n):
    print('$', end='')
    for col in range(row):
        print(' $', end='')
    print()