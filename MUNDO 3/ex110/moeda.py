def metade(x=0, form=False):
    res = x / 2
    if form:
        return moeda(res)
    else:
        return res


def dobro(x=0, form=False):
    res = x * 2
    if form:
        return moeda(res)
    else:
        return res


def aumentar(x=0, porc=0, form=False):
    res = x + (x * porc / 100)
    if form:
        return moeda(res)
    else:
        return res


def diminuir(x=0, porc=0, form=False):
    res = x - (x * porc / 100)
    if form:
        return moeda(res)
    else:
        return res


def moeda(x=0, tipom='R$'):
    return f'{tipom}{x:.2f}'.replace('.', ',')


def resumo(x=0, porcaum=0, porcdim=0):
    print('=' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('=' * 40)
    print(f'Preço analizado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{dobro(x, True)}')
    print(f'Metade do preço: \t{metade(x, True)}')
    print(f'{porcaum}% de aumento: \t{aumentar(x, porcaum, True)}')
    print(f'{porcdim}% de redução: \t{diminuir(x, porcdim, True)}')
    print('=' * 40)
