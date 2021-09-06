print('\033[1;30m-' * 50)
print('{: ^50}'.format('Sequência de Fibonacci'))
print('-' * 50)
nt = int(input('Quantos termos você quer mostrar?'))
c = 0
np = 0  # NÚMERO DO PASSADO
na = 1  # NÚMERO ATUAL
while not nt == c:
    print(np, end=' → ')
    np += na
    c += 1
    if nt != c:
        print(na, end=' → ')
        na += np
        c += 1
print('FIM')
print('-' * 50)
