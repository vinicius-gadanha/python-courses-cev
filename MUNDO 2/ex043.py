print('\033[1;30mCalculo do seu IMC,responda as perguntas abaixo:')
peso = float(input('\033[1;36mQual é seu peso? (Kg)'))
altu = float(input('Qual é a sua altura? (m)'))
imc = peso / (altu**2)
print('')
print('\033[46m{}\033[m'.format('  ' * 30))
print('\033[1;30mO seu IMC é de {:.1f}'.format(imc))
print('Sua classificação de acordo com o IMC é ', end='')
if imc < 18.5:
    print('\033[0;31mAbaixo do Peso')
elif 18 <= imc < 25:
    print('\033[1;33mPeso Ideal')
elif 25 <= imc < 30:
    print('\033[0;31mSobrepeso')
elif 30 <= imc < 40:
    print('\033[1;31mObesidade')
elif 40 < imc:
    print('\033[1;31mOBESIDADE MÓRBIDA.\n\033[4;30mProcure ajuda de um especialista.')
print('\033[46m{}\033[m'.format('  ' * 30))
