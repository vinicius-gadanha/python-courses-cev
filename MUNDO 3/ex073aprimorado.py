times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
while True:
    print('\033[1;33m{:-^40}\033[1;30m'.format(' BRASILEIRÃO 2019 '))
    print('''    [ 1 ] 5 PRIMEIROS COLOCADOS
    [ 2 ] 4 ÚLTIMOS COLOCADOS
    [ 3 ] LISTA EM ORDEM ALFABÉTICA
    [ 4 ] SABER A POSIÇÃO DE ALGUM TIME
    [ 5 ] LISTA DOS TIMES DO BRASILEIRÃO
    [ 6 ] PARAR O PROGRAMA''')
    print('\033[1;33m-\033[1;30m' * 40)
    esc = int(input('O que você quer saber?? '))
    while not 0 < esc < 7:
        esc = int(input('TENTE NOVAMENTE!! Digite o número de acordo com a sua escolha:'))
    if esc == 1:
        for pos in range(0, len(times[0:5])):
            print(f'{pos + 1:2}º {times[pos]}')
    if esc == 2:
        for pos in range(16, len(times)):
            print(f'{pos + 1:2}º {times[pos]}')
    if esc == 3:
        for pos in range(0, len(times)):
            print(f'{pos + 1:2}º {sorted(times)[pos]}')
    if esc == 4:
        time = str(input('Digite o nome do time: ')).title().strip()
        print('O {} está na {}ª posição.'.format(time, times.index(time) + 1))
    if esc == 5:
        for pos, nome in enumerate(times):
            print(f'{pos + 1:2}º {nome}')
    if esc == 6:
        break
    son = str(input('Quer continuar?? [S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar?? Digite [SIM] ou [NÃO]: ')).upper().strip()[0]
    if son == 'N':
        break
print('\033[1;33m-' * 40)
print('Tenha um bom dia e volte sempre!!!')
print('\033[1;31m{:-^40}'.format(' PROGRAMA FINALIZADO'))
