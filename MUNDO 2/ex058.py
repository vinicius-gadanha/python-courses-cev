from random import randint
from time import sleep
from playsound import playsound
vez = 1
num = randint(0, 10)
print('\033[1;30mEu vou pensar em um número de 0 a 10.Tente adivinhar...')
print('=' * 90)
esc = int(input('\033[1;35mDigite o número que eu pensei:'))
print('\033[1;30mPROCESSANDO...')
sleep(0.2)
while num != esc:
    if num > esc:
        playsound('ERROUU.mp3')
        esc = int(input('\033[1;31mERROUUU!!!\033[1;35mTENTE OUTRO NÚMERO(DICA É MAIOR):'))
    elif num < esc:
        playsound('ERROUU.mp3')
        esc = int(input('\033[1;31mERROUUU!!!\033[1;35mTENTE OUTRO NÚMERO(DICA É MENOR):'))
    vez += 1
    print('\033[1;30mPROCESSANDO...')
    sleep(0.2)
playsound('ACERTO MISERAVI.mp3')
if num == esc and vez == 1:
    print('\033[1;33mKRAI VC ACERTO O NÚMERO COM {} TENTATIVA.'.format(vez))
elif num == esc and 1 < vez <= 6:
    print('\033[1;33mBOA VC ACERTOU O NÚMERO COM {} TENTATIVAS, DEMOROU UM POUCO MAS ACERTOU.'.format(vez))
elif num == esc and vez > 6:
    print('\033[1;33mACHEI QUE VOCÊ NUNCA IA ACERTA ESSE NÚMERO, FORAM {} TENTATIVAS.'.format(vez))
print('\033[1;30m=' * 90)
