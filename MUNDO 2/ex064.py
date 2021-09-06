n = c = x = 0
while x != 999:
    x = int(input('\033[1;30mDigite um número [999 para parar]:'))
    if x != 999:
        n += x
        c += 1
print('Foram {} números digitados e a soma deles é {}.'.format(c, n))
