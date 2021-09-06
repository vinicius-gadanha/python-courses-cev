matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = sterc = maior = 0

for li in range(0, 3):
    for c in range(0, 3):
        matriz[li][c] = int(input(f'Digite um valor para [{li}, {c}]: '))
print('=' * 60)

for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[li][c]:^5}]', end='')
        if matriz[li][c] % 2 == 0:
            spar += matriz[li][c]
        if c == 2:
            sterc += matriz[li][c]
        if li == 1:
            if matriz[li][c] > maior:
                maior = matriz[li][c]
    print()

print('=' * 60)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira colunas é {sterc}.')
print(f'O maior valor da segunda linha é {maior}.')
print('=' * 60)
