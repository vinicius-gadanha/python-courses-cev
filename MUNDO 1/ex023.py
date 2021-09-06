n = int(input('\033[1;30mDigite um número de 0 a 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('')
print('\033[1;32m-'*25)
print('\033[4;30mAnalizando o número {}'.format(n))
print('\033[1;32m-'*25)
print('\033[4;30mUnidade:{:2}\nDezena:{:3}\nCentena:{:2}\nMilhar:{:3}'.format(u, d, c, m))
print('\033[1;32m-'*25)

#ns = str(n)
#print('Unidade: {}'.format(ns[3]))
#print('Dezena: {}'.format(ns[2]))
#print('Centena: {}'.format(ns[1]))
#print('Milhar: {}'.format(ns[0]))
