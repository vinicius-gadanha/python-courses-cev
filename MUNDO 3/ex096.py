def boni():
    print('=' * 50)
    print('{:^50}'.format('Controle de Terrenos:'))
    print('=' * 50)
    area(larg=float(input('LARGURA(m): ')), comp=float(input('COMPRIMETO(m): ')))
    print('=' * 50)


def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {ar}m²')


while True:
    boni()
    son = str(input('Quer continuar??[S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar??[S/N] ')).upper().strip()[0]
    if son == 'N':
        break
