print('\033[1;30m-' * 60)
print('{:^60}'.format(' BANCO VINICIM '))
print('-' * 60)
n50 = n20 = n10 = n01 = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    while not valor == 0:
        n50 = valor // 50
        valor = valor - (n50 * 50)
        if n50 >= 1:
            print(f'Total de {n50} cédulas de R$50')
            if valor == 0:
                break
        n20 = valor // 20
        valor = valor - (n20 * 20)
        if n20 >= 1:
            print(f'Total de {n20} cédulas de R$20')
            if valor == 0:
                break
        n10 = valor // 10
        valor = valor - (n10 * 10)
        if n10 >= 1:
            print(f'Total de {n10} cédulas de R$10')
            if valor == 0:
                break
        n01 = valor // 1
        valor = valor - (n01 * 1)
        print(f'Total de {n01} cédular de R$1')
    if valor == 0:
        break
print('-' * 60)
print('Tenha um bom dia!!! Volte sempre ao BANCO VINICIM!!!')
