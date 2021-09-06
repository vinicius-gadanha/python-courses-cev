from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[-1], end=' ')
        sleep(0.4)
    print('PRONTO!!')


def somapar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {lista}, temos {s}.')


numeros = []
sorteia(numeros)
somapar(numeros)
