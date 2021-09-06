def leiaint(msg):
    print('=' * 40)
    num = str(input(msg)).strip()
    while not num.isnumeric():
        print('\033[0;31mERRO!! Digite um número inteiro válido.\033[m')
        num = str(input(msg)).strip()
    return int(num)


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('=' * 40)
