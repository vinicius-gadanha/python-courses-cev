print('\033[1;35m{:_^80}'.format(' PALÍNDROMO '))
fra = str(input('\033[1;30mDigite uma frase:')).upper().strip().split()
jun1 = ''.join(fra)
jun2 = str('')
for c in range(len(jun1) - 1, -1, -1):
    jun2 += jun1[c]
print('O inverso de {} é {}'.format(jun1, jun2))
if jun1 == jun2:
    print('Temos um palíndromo!!!')
else:
    print('A frase digitada não é um palíndromo!!!')
print('\033[1;35m_' * 80)
# FORMA MUITO MAIS FACIL
# frase = input("Qual a frase? ").upper().replace(" ", "")
# if frase == frase[::-1]:
# print("A frase é um palíndromo")
# else:
# print("A frase não é um palíndromo")
# print(frase)
