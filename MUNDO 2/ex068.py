from random import randint
cpu = 0
c = 0
print('\033[1;31m{:-^55}'.format(' JOGO ÍMPAR OU PAR '))
while True:
    n = int(input('\033[1;30mDiga um valor:'))
    cpu = randint(1, 10)
    total = n + cpu
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {cpu}. Total de {total},', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if (total % 2 == 0 and tipo == 'P') or (total % 2 != 0 and tipo == 'I'):
        print('Você VENCEU!!!\nVamos jogar novamente...')
        print('\033[1;31m-\033[1;30m' * 55)
        c += 1
    else:
        print('Você PERDEU!!!')
        break
print('\033[1;31m-' * 55)
if c > 1:
    print(f'\033[1;31mGAME OVER!!!\033[1;30m Você venceu {c} vezes.')
elif c == 1:
    print(f'\033[1;31mGAME OVER!!!\033[1;30m Você venceu {c} vez.')
else:
    print('\033[1;31mGAME OVER!!!\033[1;30m Você não ganhou nenhuma partida.')
