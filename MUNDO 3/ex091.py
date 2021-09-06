from random import randint
from time import sleep
from operator import itemgetter

rank = list()
jogo = dict()
print('=' * 30)
print('Valores sorteados:')
for c in range(1, 5):
    jogo[f'Jogador{c}'] = randint(1, 6)
    print(f'   O Jogador{c} tirou: {jogo[f"Jogador{c}"]}')
    sleep(0.4)
print('=' * 30)

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('{:^30}'.format('Ranking dos jogadores:'))
print('=' * 30)

for i, v in enumerate(rank):
    print('{:^30}'.format(f'{i+1}º lugar: {v[0]}({v[1]})'))
    sleep(0.4)
print('=' * 30)
