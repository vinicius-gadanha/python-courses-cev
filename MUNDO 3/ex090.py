ficha = {'Nome': str(input('Nome: ')).capitalize().strip()}
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))

if ficha['Média'] >= 7:
    ficha['Situação'] = '\033[1;33mAprovado'
elif 5 <= ficha['Média'] < 7:
    ficha['Situação'] = '\033[0;31mRecuperação'
else:
    ficha['Situação'] = '\033[1;31mReprovado'

print('=' * 40)
for k, v in ficha.items():
    print(f'{k} = {v}')
print('\033[m=' * 40)
