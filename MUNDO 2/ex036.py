print('\033[1;36mBom dia, para você saber se está autorizado a pegar um emprestimo responda as perguntas abaixo.')
val = float(input('\033[1;30mQual o valor da casa que quer comprar?'))
sal = float(input('Qual é o valor do seu salário?'))
ano = float(input('Em quantos anos você pretende pagar o empréstimo?'))
prm = float(val / (ano * 12))
print('')
if prm > (sal * 30 / 100):
    print('\033[41m{}\033[m'.format('  ' * 50))
    print('Desculpa, mas infelizmente o empréstimo foi \033[4;30mNEGADO\033[m.')
    print('Porque a prestação mensal de R${:.2f}, excede os 30% do seu sálario que é R${:.2f}'
          .format(prm, sal * 30 / 100))
    print('\033[41m{}\033[m'.format('  ' * 50))
else:
    print('\033[46m{}\033[m'.format('  ' * 50))
    print('Parabéns, o empréstimo foi \033[4;30mAPROVADO\033[m!')
    print('O preço que você terá que pagar todo mês é R${:.2f}'.format(prm))
    print('Muito obrigado por escolhe nossa empresa, e aproveite sua nova casa!')
    print('\033[46m{}\033[m'.format('  ' * 50))
