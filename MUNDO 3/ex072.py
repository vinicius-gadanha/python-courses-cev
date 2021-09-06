numext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('\033[1;30mDigite um número entre 0 e 20: '))
    while not 0 <= num <= 20:
        num = int(input('TENTE NOVAMENTE!!! Digite um número de 0 a 20: '))
    print(f'Você digitou o número {numext[num]}.')
    son = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while son not in 'SN':
        son = str(input('TENTE NOVAMENTE!!!Você quer continuar? [S/N] ')).upper().strip()[0]
    if son == 'N':
        break
print('{:-^30}'.format('PROGRAMA FINALIZADO'))
