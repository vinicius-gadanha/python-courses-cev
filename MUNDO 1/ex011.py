l = float(input('\033[1;36mQual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = (l*h)
q = (a/2)
print('\033[0;36mA área da parede é \033[1;33m{:.2f}m²'
      '\n\033[0;36mA quantidade de tinta exata para pintar essa parede é \033[1;33m{:.2f} litros.'.format(a, q))
