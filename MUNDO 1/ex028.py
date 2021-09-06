import random
import playsound
from time import sleep
from termcolor import colored
n = (0, 1, 2, 3, 4, 5)
num = random.choice(n)
#num = randint(0, 5)
#print('O número aleátorio é {}.'.format(num))
print(colored('=', 'yellow')*60)
print('Vou pensar em um número entre 0 e 5.Tente Adivinhar...')
print(colored('=', 'yellow')*60)
us = int(input('Em que número eu pensei?'))
print(colored('PROCESSANDO...', 'magenta'))
sleep(1)
if num == us:
    print(colored('KRAI SE ACERTO O NÚMERO', 'green'))
    playsound.playsound('ex028.mp3')
else:
    print(colored('ERROUUUU, o número que eu pensei foi {}.', 'red').format(num))
    playsound.playsound('ex021.mp3')
