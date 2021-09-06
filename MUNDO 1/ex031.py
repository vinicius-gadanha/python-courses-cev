dis = int(input('\033[1;30mQual a distância de sua viagem em Km?'))
if dis > 200:
    p1 = float(dis * 0.45)
    print('O preço da sua viagem será de R${:.2f}.'.format(p1))
else:
    p1 = float(dis * 0.50)
    print('O preço da sua viagem será de R${:.2f}.'.format(p1))
# p1 = dis * 0.45 if dis > 200 else disc * 045
