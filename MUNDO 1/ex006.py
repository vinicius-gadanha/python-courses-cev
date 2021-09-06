n = int(input('\033[1;36mDigite um numero:'))
print('\033[0;36mO dobro é \033[1;31m{}\n\033[0;36mO triplo é \033[1;35m{}\n\033[0;36mSua raiz quadrada é '
      '\033[1;33m{:.3f}.'.format(n*2, n*3, n**(1/2)))
