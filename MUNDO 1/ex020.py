import random
a1 = input('\033[1;31mAluno 1:')
a2 = input('\033[1;33mAluno 2:')
a3 = input('\033[1;36mAluno 3:')
a4 = input('\033[1;35mAluno 4:')
li = [a1, a2, a3, a4]
cl = random.shuffle(li)
print(' ')
print('\033[1;30mA ordem dos alunos que iram apresentar o trabalho vai ser:\033[4;32m{}'.format(li))
