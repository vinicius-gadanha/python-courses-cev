from time import sleep
from random import randint


def maior(*num):
    print('=' * 50)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('Nenhum valor foi passado.')
    else:
        print(f'O maior valor informado foi {max(num)}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
