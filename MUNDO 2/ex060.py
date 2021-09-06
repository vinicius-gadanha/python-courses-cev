n = int(input('\033[1;30mDigite um número para calcular seu FATORIAL:'))
f = n
print('\033[1;35m-' * 60)
print('{}!\033[1;30m ='.format(n), end=' ')
while n != 1:
    print(n, end=' x ')
    n -= 1
    f *= n
print('1 = \033[1;35m{}'.format(f))
print('\033[1;35m-' * 60)
