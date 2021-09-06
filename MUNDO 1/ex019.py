import random
a1 = input('\033[1;31mPrimeiro Aluno:')
a2 = input('\033[1;36mSegundo Aluno:')
a3 = input('\033[1;33mTerceiro Aluno:')
a4 = input('\033[1;35mQuarto Aluno:')
so = random.choice([a1, a2, a3, a4])
print(' ')
print('\033[1;30mO aluno que irá apagar o quadro será o \033[4;37m{}.'.format(so))
