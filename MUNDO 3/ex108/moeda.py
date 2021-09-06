def metade(x=0):
    res = x / 2
    return res


def dobro(x=0):
    res = x * 2
    return res


def aumentar(x=0, porc=0):
    res = x + (x * porc / 100)
    return res


def diminuir(x=0, porc=0):
    res = x - (x * porc / 100)
    return res


def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')
