print('\033[1;30m{:_^40}'.format(' O NÚMERO É PRIMO OU NÃO '))
c = 0
count = 0
num = int(input('\033[1;36mDigite um número inteiro:'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[35m', end=' ')
        count = count + 1
    else:
        print('\033[1;30m', end=' ')
    print(c, end=' ')
print('\n\033[1;36mO número {} foi divisível {} vezes.'.format(num, count))
if count == 2:
    print('\033[1;36mO número {} é PRIMO'.format(num))
else:
    print('\033[1;36mO número {} NÃO é PRIMO'.format(num))
print('\033[1;30m_' * 40)
