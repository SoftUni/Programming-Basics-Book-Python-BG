# Квадратна рамка

n = int(input())

# printing the top row: + - - - +
print('+', end='')
for i in range(n - 2):
    print(' -', end='')
print(' +')

# printing the mid rows: | - - - |
for row in range(n - 2):
    print('|', end='')
    for col in range(n - 2):
        print(' -', end='')
    print(' |')

# printing the bottom row: + - - - +
print('+', end='')
for i in range(n - 2):
    print(' -', end='')
print(' +')