jogador = dict()
g = list()

print('=' * 50)
print('{:^50}'.format('RENDIMENTO DO JOGADOR'))
print('=' * 50)
jogador['nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
nump = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
print('=' * 50)

for c in range(0, nump):
    g.append(int(input(f'Quantos gols fez na {c + 1}ºPARTIDA: ')))
jogador['gols'] = g[:]
jogador['total'] = sum(g)
print('=' * 50)

for k, v in jogador.items():
    print(f'{k} = {v}')
print('=' * 50)

print(f'O jogador {jogador["nome"]} jogou {nump} partidas.')
for pos, ng in enumerate(g):
    print((' ' * 4), f' =>{pos + 1}ºPARTIDA: ')
    print((' ' * 11), f'->Nº de GOLS: {ng}')
print(f'Foi um total de {jogador["total"]} gols.')
print('=' * 50)
print(jogador)
