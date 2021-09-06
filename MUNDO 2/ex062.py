print('\033[1;30m{:-^80}'.format(' GERADOR DE P.A. '))
t1 = int(input('\033[1;33mPrimeiro termo:'))
r = int(input('Razão:\033[1;30m'))
print('-' * 80)
c = 0
x = 10
nt = 10
while x != 0:
    while not c == x:
        print(t1, end=' -> ')
        t1 += r
        c += 1
    if c == x:
        c = 0
        x = int(input('\033[1;33mPAUSA\nQuantos termos você quer mostrar a mais?\033[1;30m'))
        nt += x
        print('-' * 80)
print('Progressão finalizada com \033[1;33m{}\033[1;30m termos mostrados.'.format(nt))
print('-' * 80)
