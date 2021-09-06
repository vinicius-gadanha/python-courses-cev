lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    son = str(input('Quer continuar??? [S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('TENTE NOVAMENTE!! Quer continuar?? [S/N] '))
    if son == 'N':
        break
pares = []
impares = []
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('===' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')
print('===' * 30)
