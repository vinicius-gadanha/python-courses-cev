print('\033[1;33m{:-^54}\033[1;30m'.format(' LOJAS VINICIM '))
tot = mmil = menor = 0
nome = ' '
while True:
    prod = str(input('Nome do Produto: ')).strip().lower()
    prco = float(input('Preço: R$'))
    tot += prco
    if prco >= 1000:
        mmil += 1
    if menor == 0 or prco < menor:
        menor = prco
        nome = prod
    son = ' '
    while son not in 'SsNn':
        son = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if son == 'N':
        break
print('\033[1;33m{:-^54}\033[1;30m'.format(' FIM DA COMPRA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Número de produtos custando mais de R$1000.00: {mmil}')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
print('\033[1;33m-' * 54)
