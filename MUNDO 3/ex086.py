num = [[], [], []]
lin = [0, 1, 2]
x = y = 0

while x < 3:
    for c in lin:
        num[x].append(int(input(f'Digite um valor para [{x}, {c}]: ')))
    x += 1

print('=' * 35)

while y < 3:
    for c in lin:
        print(f'[{num[y][c]:^5}]', end='')
    print()
    y += 1

print('=' * 35)
