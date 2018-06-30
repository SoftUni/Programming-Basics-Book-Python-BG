# Слънчеви очила

n = int(input())

# printing the top part
print('*' * (2 * n), end='')
print(' ' * n, end='')
print('*' * (2 * n))

# printing the middle part
for i in range(n - 2):
    # TODO: print *////////*
    print('*' + "/" * (2 * n - 2) + '*', end='')

    if i == (n - 1) // 2 - 1:
        print('|' * n, end='')
    else:
        print(' ' * n, end='')

    # TODO: print *////////*

    print('*' + "/" * (2 * n - 2) + '*', end='')
    print()

# printing the bottom part
print('*' * (2 * n), end='')
print(' ' * n, end='')
print('*' * (2 * n))

