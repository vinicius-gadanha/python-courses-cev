num = int(input('\033[1;30mDigite um número para ver sua tabuada:'))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num * c))
