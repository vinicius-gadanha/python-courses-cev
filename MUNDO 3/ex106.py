def escreva(txt):
    print('=' * (len(txt) + 2))
    print(f' {txt}')
    print('=' * (len(txt) + 2))


def ajuda(x):
    print('\033[1;30;45m', end='')
    escreva(f'Acessando o manual do comando <<<"{x}">>>')
    print('\033[1;31;40m', end='')
    from time import sleep
    sleep(1)
    help(x)


# Programa Principal
while True:
    print('\033[1;30;44m', end='')
    escreva('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    fb = str(input('Função ou Biblioteca: ')).lower().strip()
    if fb == 'fim':
        print('\033[1;30;41m-PROGRAMA ENCERRADO-')
        break
    else:
        ajuda(fb)
        print('\033[m', end='')
