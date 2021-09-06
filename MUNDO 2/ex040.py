n1 = float(input('\033[1;36mPrimeira nota:'))
n2 = float(input('\033[1;36mSegunda nota:'))
me = (n1 + n2) / 2
print('\033[40m{}\033[m'.format('  ' * 15))
print('\033[1;30mA média das notas é {:.1f}.'.format(me))
if me < 5.0:
    print('Média abaixo de 5.0\n\033[1;31m'
          'REPROVADO')
elif 5.0 <= me <= 6.9:
    print('\033[1;30mMédia entre 5.0 e 6.9\n\033[4;31m'
          'RECUPERAÇÃO')
elif me >= 7.0:
    print('\033[1;30mMédia igual ou acima que 7.0\n\033[1;33m'
          'APROVADO')
print('\033[40m{}\033[m'.format('  ' * 15))
