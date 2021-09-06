s = 0
cont = 0
for n in range(3, 499, 6):
    # print(n, end=' ')
    s += n
    cont += 1
print("A soma de todos os {} valores é {}.".format(cont, s))
