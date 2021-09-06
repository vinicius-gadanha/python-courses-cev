galera = list()
dados = list()
pesados = list()
leves = list()
maior = 0
menor = 99999999

while True:
    dados.append(str(input('Nome: ').capitalize()))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    son = str(input('Quer continuar?? [S/N]: ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar?? [S/N]: ')).upper().strip()[0]
    if son in 'Nn':
        break

for p in galera:
    if p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]

for p in galera:
    if p[1] == maior:
        pesados.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])

print('==' * 40)
print(f'Número total de pessoas cadastradas: {len(galera)}')
print(f'O maior peso foi de {maior} Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor} Kg. Peso de {leves}')
print('==' * 40)
