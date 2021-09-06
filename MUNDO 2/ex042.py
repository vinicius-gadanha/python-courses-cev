r1 = float(input('\033[1;36mPrimeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
print(' \033[1;30m')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓCELES')
else:
    print('Os segmentos NÃO FORMAM um triângulo.')
