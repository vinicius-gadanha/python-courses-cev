def fatorial(n, show=False):
    """
    =>Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    while not n == 0:
        f *= n
        if show:
            print(n, end='')
            if n > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        n -= 1
    return f


print('=' * 40)
num = int(input('Digite um número: '))
print(fatorial(num, show=True))
print('=' * 40)
