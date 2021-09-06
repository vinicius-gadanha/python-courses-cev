from random import randint
from time import sleep

print('=' * 60)
print('{:^60}'.format('GERADOR DE JOGOS'))
print('{:^60}'.format('PARA MEGASENA'))
print('=' * 60)

njogos = int(input('Digite a quantidade de jogos que você quer gerar: '))

print('=' * 60)
print('{:^60}'.format(f'GERANDO {njogos} JOGOS...'))
print('=' * 60)

num = []
x = 0

while not njogos == x:
    x += 1
    while len(num) != 6:
        nr = randint(1, 60)
        if num.count(nr) < 2:
            num.append(nr)
    print(f'Jogo {x:^2}: {num}')
    num.clear()
    sleep(0.4)

print('=' * 60)
print('{:^60}'.format('BOA SORTE!!!'))
print('=' * 60)
