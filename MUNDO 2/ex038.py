print('\033[1;30mDigite dois números inteiros:')
n1 = int(input('\033[1;36mPrimeiro Número:'))
n2 = int(input('\033[1;36mSegundo número:'))
print('')
print(' \n\033[46m{}\033[m'.format('  ' * 30))
if n1 > n2:
    print('\033[1;30mO primeiro número é maior.')
    print('{} > {}'.format(n1, n2))
elif n1 < n2:
    print('\033[1;30mO segundo número é maior.')
    print('{} > {}'.format(n2, n1))
else:
    print('\033[1;30mO primeiro e o segundo número são iguais.')
    print('{} = {}'.format(n1, n2))
print('\033[46m{}\033[m'.format('  ' * 30))
