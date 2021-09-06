n = float(input('\033[1;36mQual o preço do produto? R$'))
p = n * (95 / 100)
# outra maneira é n - (n*5/100)
print('\033[0;36mO preço deste produto é \033[1;31mR${:.2f} \033[0;36m,mas com a promoção de'
      ' 5% de desconto ele irá custar \033[1;33mR${:.2f}'.format(n, p))
