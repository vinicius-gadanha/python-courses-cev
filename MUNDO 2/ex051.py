print('\033[1;33m{:_^80}'.format(' 10 TERMOS PROGRESSÃO ARITIMÉTICA '))
n1 = int(input('\033[1;30mPrimeiro termo:'))
r = int(input('Razão:'))
x = n1 + (10 * r)
for c in range(n1, x, r):
    print(c, end=' -> ')
print('ACABOU')
print('\033[1;33m_' * 80)
