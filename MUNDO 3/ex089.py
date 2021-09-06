lista = []
dados = []
nomes = []
notas = []

while True:
    print('=' * 50)
    nomes.append(str(input('Nome: ').capitalize().strip()))
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    notas.append((notas[0] + notas[1]) / 2)
    dados.append(nomes[:])
    dados.append(notas[:])
    lista.append(dados[:])
    nomes.clear()
    notas.clear()
    dados.clear()
    son = str(input('Quer continuar?? [S/N]: ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('Quer continuar?? [S/N]: ')).upper().strip()[0]
    if son == 'N':
        break

print('=' * 50)
print('No.  {:<15}MÉDIA'.format('NOME:'))
print('=' * 50)
for c in range(0, len(lista)):
    print('{}º   {:<15}{:.1f}'.format(c+1, lista[c][0][0], float(lista[c][1][2])))
print('=' * 50)

x = int(input('Mostrar notas de qual aluno?(999 interrrompe): '))
while x != 999:
    if x <= len(lista):
        print(f'As notas de {lista[x - 1][0][0]} são {lista[x - 1][1][:2]}')
        print('=' * 50)
        x = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    else:
        print('NÚMERO DO ALUNO NÃO ENCONTRADO.')
        x = int(input('Mostrar notas de qual aluno?(999 interrompe): '))

print('=' * 50)
print('{:^50}'.format('PROGRAMA FINALIZADO'))
print('=' * 50)
