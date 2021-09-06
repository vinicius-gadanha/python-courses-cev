times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-' * 80)
print(f'Os cinco primeiros são {times[0:5]}')
print('-' * 80)
print(f'Os quatro últimos são {times[-4:]}')
print('-' * 80)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 80)
print('O Chapecoense está na {}ª posição.'.format(times.index('Chapecoense') + 1))
