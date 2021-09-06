n = float(input('\033[1;36mQuantos reais voce tem? R$'))
d = n / 5.44
print('\033[0;36mCom \033[1;33mR${:.2f}\033[0;36m voce pode comprar \033[1;33mUS${:.2f}'.format(n, d))
