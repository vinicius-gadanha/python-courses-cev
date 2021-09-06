pessoas = list()
pessoa = dict()

print('=' * 60)
print('{:^60}'.format('CADASTRANDO USUÁRIOS'))
print('=' * 60)

while True:
    pessoa['NOME'] = str(input('Nome: ')).capitalize().strip()
    pessoa['SEXO'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    while pessoa['SEXO'] not in 'MF':
        print('ERRO!! Por favor, digite apenas M ou F.')
        pessoa['SEXO'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    pessoa['IDADE'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    son = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while son not in 'SN':
        son = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    print('=' * 60)
    if son == 'N':
        break

soma = 0
for c in range(0, len(pessoas)):
    soma += pessoas[c]['IDADE']

print(f'  => Número de arquivo cadastradas: {len(pessoas)}')
print(f'  => Média da idade das arquivo cadastradas: {soma / len(pessoas):.2f} anos.')
print(f'  => Mulheres cadastradas: -', end='')

for c in range(0, len(pessoas)):
    if pessoas[c]['SEXO'] == 'F':
        print(pessoas[c]['NOME'], end=' - ')
print()

print('  => Lista das arquivo que estão acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]['IDADE'] > (soma / len(pessoas)):
        print(' ' * 10, '=' * 45)
        print(' ' * 11, end='')
        for k, v in pessoas[c].items():
            print(f'-> {k} = {v}', end='; ')
        print()

print('=' * 60)
print('{:^60}'.format('ENCERRADO'))
print('=' * 60)
