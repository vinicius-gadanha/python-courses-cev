n = m = 0
c = 10
while True:
    if c == 10:
        print('-' * 50)
        n = int(input('\033[1;30mQuer ver a tabuada de qual valor?'))
        c = 0
        print('-' * 50)
    if n < 0:
        break
    else:
        c += 1
        m = n * c
        print(f'{n} x {c:2} = {m}')
print('\033[1;33mPROGRAMA TABUADA ENCERRADO. Volte sempre!')
