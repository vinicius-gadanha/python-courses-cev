num = (int(input('\033[1;30mDigite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print('-' * 50)
print(f'Total de vezes que o número 9 apareceu: {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end=' ')
for c in range(0, 4):
    if num[c] % 2 == 0:
        print(num[c], end=' ')
print('')
print('-' * 50)
