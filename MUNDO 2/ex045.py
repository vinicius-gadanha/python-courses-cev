import random
from time import sleep

print('\033[1;30m{}{}{}'.format('=' * 20, '\033[1;35m JO \033[1;36mKEN \033[1;33mPÔ \033[1;30m', '=' * 20))
print('''Suas opções:
[ A ] PEDRA
[ B ] PAPEL
[ C ] TESOURA''')
player = str(input('Qual é a sua jogada?')).lower()
if player == 'a':
    player = 'Pedra'
elif player == 'b':
    player = 'Papel'
elif player == 'c':
    player = 'Tesoura'
print('\033[1;35mJO')
sleep(1)
print('\033[1;36mKEN')
sleep(1)
print('\033[1;33mPÔ')
sleep(1)
a = 'Pedra'
b = 'Papel'
c = 'TESOURA'
x = (a, b, c)
cpu = random.choice(x)
resultado = ''
print('\033[1;30m=' * 51)
print('\033[1;35mComputador jogou {}\n\033[1;36mJogador jogou {}'.format(cpu, player))
if (player == a and cpu == b) or (player == b and cpu == c) or (player == c and cpu == a):
    resultado = '\033[1;35mCPU VENCEU'
elif (player == a and cpu == c) or (player == c and cpu == b) or (player == a and cpu == c):
    resultado = '\033[1;36mJOGADOR VENCEU'
elif player == cpu:
    resultado = '\033[1;33mEMPATOU'
else:
    print('\033[1;31mERRO:TENTE NOVAMENTE\033[m')
print('\033[1;30m=' * 51)
print(resultado)
