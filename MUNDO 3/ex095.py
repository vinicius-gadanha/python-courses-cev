jogadores = list()
jogador = dict()
g = list()

print('=' * 70)
print('{:^70}'.format('RENDIMENTO DO JOGADOR'))
print('=' * 70)

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    npart = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, npart):
        g.append(int(input(f'Quantos gols na {c + 1}ºPARTIDA: ')))
    jogador['gols'] = g[:]
    jogador['total'] = sum(g)
    jogadores.append(jogador.copy())
    jogador.clear()
    g.clear()
    son = str(input('Quer continuar?? [S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar?? [S/N] ')).upper().strip()[0]
    print('=' * 70)
    if son == 'N':
        break

n = 0
print('-' * 50)
print('{:<6}{:<12}{:<15}{:<12}'.format('Cod.:', 'Nome:', 'Gols:', 'Total:'))
print('-' * 50)
for j in jogadores:
    print(f'{n:>5} {j["nome"]:<12}{j["gols"]!s:<15}{j["total"]:<12}')
    n += 1
print('-' * 50)

while True:
    cod = int(input('Digite o código do jogador para saber mais(999 interrompe): '))
    print('=' * 70)
    if cod < len(jogadores):
        print('-' * 42)
        print(f'   =>LEVANTAMENTO DO {jogadores[cod]["nome"].upper()}:')
        for p, v in enumerate(jogadores[cod]['gols']):
            print(f'            ->Na {p}ºPARTIDA: {v} gols')
        print('-' * 42)
    elif cod > len(jogadores) - 1 and cod != 999:
        print('ERRO!! Código inválido.')
    print('=' * 70)
    if cod == 999:
        break

print('{:^70}'.format('PROGRAMA FINALIZADO'))
print('=' * 70)
