# Коледна елха

n = int(input())

for i in range(n + 1):
    stars = '*' * i
    spaces = ' ' * (n - i)
    print(spaces, end='')
    print(stars, end='')
    print(' | ', end='')
    print(stars, end='')
    print(spaces)
