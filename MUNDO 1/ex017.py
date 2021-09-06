import math

ca = float(input('\033[1;30mCateto Adjacente em cm:'))
co = float(input('\033[1;30mCateto Oposto em cm:'))
hi = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
print(' ')
print('\033[0;30mA hipotenusa desse triangulo é \033[1;33m{:.2f}'.format(hi))
# poderia ser math.hypot(ca, co)
