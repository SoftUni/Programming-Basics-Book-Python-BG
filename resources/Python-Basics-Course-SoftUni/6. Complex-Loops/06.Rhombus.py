# Ромбче от звездички

n = int(input())

for row in range(1, n + 1):
    for col in range(1, (n - row) + 1):
        print(' ', end='')
    print('*', end='')
    for col in range(1, row):
        print(' *', end='')
    print()

# TODO: print the bottom side of the rhombus
for row in reversed(range(1, n)):
    print(' ' * (n - row), end='')
    print('*', end='')
    print(' *' * (row - 1))
