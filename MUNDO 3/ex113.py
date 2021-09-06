def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número INTEIRO válido.\033[m')
        else:
            break
    return n


def leiafloat(txt):
    while True:
        n = str(input(txt)).strip().replace(',', '.')
        try:
            n = float(n)
        except:
            print('\033[0;31mERRO: Por favor, digite um número REAL válido.\033[m')
        else:
            break
    return n


nint = leiaint('Digite um número INTEIRO: ')
nflo = leiafloat('Digite um número REAL: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {nflo}')
