from time import sleep


def contador(a, b, x):
    if (a > b and x > 0) or (a < b and x < 0):
        x = - x
    if x == 0:
        if a > b:
            x = -1
        elif a < b:
            x = 1
    print('=' * 50)
    if x > 0:
        print(f'Contagem de {a} até {b} de {x} em {x}:')
        for c in range(a, b+1, x):
            print(c, end=' ')
            sleep(0.4)
        print('FIM!!')
    elif x < 0:
        print(f'Contagem de {a} até {b} de {-x} em {-x}:')
        for c in range(a, b-1, x):
            print(c, end=' ')
            sleep(0.4)
        print('FIM!!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('=' * 50)
print('Agora é sua vez de personalizar a contagem!')
contador(a=int(input('Início: ')),
         b=int(input('Fim:    ')),
         x=int(input('Passo:  ')))
print('=' * 50)
