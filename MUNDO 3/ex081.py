lista = []
n = 0
while True:
    lista.append(int(input('Digite um número: ')))
    son = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('TENTE NOVAMENTE. Quer continuar? [S/N] ')).upper().strip()[0]
    if son == 'N':
        break
print('=' * 80)
print(f'A quantidade de números digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista de valores, ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e está na posição: ', end='')
    for pos, num in enumerate(lista):
        if num == 5:
            print(f'{pos}...', end=' ')
            print()
else:
    print('O valor 5 não foi encontrado na lista!')
print('=' * 80)
