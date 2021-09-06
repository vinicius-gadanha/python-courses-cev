n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print('\033[36mA soma entre \033[1;31m{}\033[0;36m e \033[1;31m{}\033[0;36m é \033[1;33m{}\033[0;36m.Certo?\033[m'
      .format(n1, n2, s))
