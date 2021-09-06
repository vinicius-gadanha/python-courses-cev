from random import randint
num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'\033[1;30mOs valores sorteados foram:', end=' ')
for c in range(0, len(num)):
    print(num[c], end=' ')
num2 = sorted(num)
print(f'\nO maior valor sorteado foi \033[1;35m{num2[-1]}.')
print(f'\033[1;30mO menor valor sorteado foi \033[1;35m{num2[0]}.')

# print(f'O maior valor sorteado foi {max(num)}')
# print(f'O menor valor sorteado foi {min(num)}')
