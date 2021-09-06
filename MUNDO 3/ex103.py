def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('=' * 60)
jogador = str(input('Nome do Jogador: ')).strip().capitalize()
ngols = str(input('Número de Gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if jogador == '':
    print(ficha(gols=ngols))
else:
    print(ficha(jogador, ngols))
print('=' * 60)
