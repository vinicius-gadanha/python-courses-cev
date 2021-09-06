s = c = 0
while True:
    n = int(input('Digite um valor (999 PARA PARAR):'))
    if n == 999:
        break
    c += 1
    s += n
print(f'A somo dos {c} valores foi {s}!')
