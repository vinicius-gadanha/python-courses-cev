m = f = tm = tf = 0
while True:
    print('\033[1;30m-' * 50)
    print('\033[1;35m{:-^50}\033[1;30m'.format(' CADASTRE UMA PESSOA '))
    print('-' * 50)
    idade = int(input('\033[1;35mIdade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if sexo == 'M':
            m += 1
        if sexo == 'F':
            f += 1
            if idade <= 20:
                tf += 1
        if idade >= 18:
            tm += 1
    son = ' '
    while son not in 'SsNn':
        son = str(input('Quer continuar?[S/N]\033[1;30m ')).strip().upper()[0]
    if son == 'N':
        break
print('-' * 50)
print('\033[1;31m{:-^50}\033[1;30m'.format(' FIM DO PROGRAMA '))
print('-' * 50)
print(f'Total de pessoas com mais de 18 anos: {tm}')
print(f'Total de homens cadastrados: {m}')
print(f'Total de mulheres com menos de 20 anos: {tf}')
print('-' * 50)
