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
