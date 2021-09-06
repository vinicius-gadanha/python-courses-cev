valores = list()
while True:
    valores.append(int(input('Digite um valor:')))
    if valores.count(valores[-1]) == 2:
        print('Valor duplicado! Não vou adicionar...')
        valores.pop()
    else:
        print('Valor adicionado com sucesso...')
    print('=' * 50)
    son = str(input('Quer continuar?? [S/N]: ')).strip().upper()[0]
    while son not in 'SN':
        son = str(input('TENTE NOVAMENTE. Digite SIM ou NÃO: ')).strip().upper()[0]
    if son == 'N':
        break
print('=' * 50)
print(f'Você digitou os valores {sorted(valores)}')
