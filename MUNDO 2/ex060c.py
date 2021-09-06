from math import factorial
n = int(input('\033[1;30mDigite um número para calcular seu FATORIAL:'))
f = factorial(n)
print('\033[1;35m-' * 60)
print('{}! \033[1;30m= '.format(n), end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' =', end='')
print('\033[1;35m', f)
print('-' * 60)
