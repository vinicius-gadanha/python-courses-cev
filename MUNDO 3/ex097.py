def escreva(txt):
    print('=' * (len(txt) + 2))
    print(f' {txt}')
    print('=' * (len(txt) + 2))


# Programa Principal
while True:
    escreva(str(input('Digite alguma coisa: ')))
    son = str(input('Quer continuar??[S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar??[S/N] ')).upper().strip()[0]
    if son == 'N':
        break
