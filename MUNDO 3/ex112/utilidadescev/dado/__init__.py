def leiadinheiro(txt):
    valido = False
    while not valido:
        valor = str(input(txt)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um preço inválido!!\033[m')
        else:
            return float(valor)
