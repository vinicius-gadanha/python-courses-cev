print('\033[1;36m{} {} {}'.format('='*20, 'LOJAS VINICIM', '='*20))
val = float(input('\033[0;36mPreço das compras: R$'))
print('\033[1;30mFORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão'
      '\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
ecl = int(input('\033[0;36mQual será a opção?'))
if ecl == 1:
    print('\033[1;30mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val, val - (val * 10 / 100)))
elif ecl == 2:
    print('\033[1;30mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val, val - (val * 5 / 100)))
elif ecl == 3:
    print('\033[1;30mSua compra vai custar R${:.2f}, e será parcelada em 2x de R${:.2f} SEM JUROS'.format(val, val / 2))
elif ecl == 4:
    parc = int(input('Quantas parcelas?'))
    valf = float(val + (val * 20 / 100))
    print('\033[1;30mSua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, valf / parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val, valf))
else:
    print('\033[1;31mOPÇÃO INVALIDADE DE PAGAMENTO.Tente novamente!')
