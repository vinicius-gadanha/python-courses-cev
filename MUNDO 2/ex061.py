print('\033[1;30m{:-^80}'.format(' GERADOR DE P.A. '))
t1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
c = 0
print('{} -> '.format(t1), end='')
while not c == 9:
    t1 += r
    c += 1
    print(t1, end=' -> ')
print('FIM')
print('-' * 80)
