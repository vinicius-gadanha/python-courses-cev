from time import sleep
print('\033[1;30m{:-^50}'.format(' MENU DE OPÇÕES: '))
n1 = float(input('\033[1;36mPrimeiro Valor:'))
n2 = float(input('Segundo Valor:'))
sair = 0
while sair != 5:
    print('''\033[1;30m    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    sair = int(input('\033[1;36m>>>>> Qual é a sua opção?\033[1;30m'))
    if sair == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif sair == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif sair == 3:
        if n1 > n2:
            print('O número maior entre {} e {} é {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('O número maior entre {} e {} é {}.'.format(n1, n2, n2))
        else:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif sair == 4:
        print('\033[1;36mInforme os números novamente:')
        n1 = float(input('Primeiro valor:'))
        n2 = float(input('Segundo valor:'))
    elif sair == 5:
        print('\033[1;31mFinalizando...')
        sleep(1)
    else:
        print('\033[1;31mOpção inválida. Tente novamente!!')
print('\033[1;30m-' * 50)
print('\033[1;33mFim do programa! Volte sempre!')
print('\033[1;30m-' * 50)
