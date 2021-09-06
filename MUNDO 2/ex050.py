cont = 0
s = 0
for c in range(1, 7):
    num = int(input('\033[1;30mDigite o {}º valor:'.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('')
if cont > 1:
    print('Você informo {} números pares, e as soma deles é {}.'.format(cont, s))
elif cont == 1:
    print('Você informo {} número par, que é o número {}.'.format(cont, s))
elif cont < 1:
    print('Você não informou nenhum número par.')
