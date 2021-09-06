print('{:-^80}'.format(' \033[1;33mMAIOR E MENOR VALORES\033[1;30m '))
maior = menor = media = 0
c = 0
x = 'S'
while 'N' not in x:
    if x == 'S':
        n = int(input('Digite um número:'))
        media += n
        c += 1
        if c == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        x = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if x != 'S' and x != 'N':
        x = str(input('\033[1;31mOpção inválida!\033[1;30mDigite SIM ou NÃO para continuar.')).strip().upper()[0]
print('-' * 80)
print('\033[1;33mVocê digitou {} números e a média foi {:.2f}'.format(c, media / c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('\033[1;30m-' * 80)
