from datetime import date
from time import sleep

print('\033[1;30mInforme seu nome completo, o seu sexo e o ano em que nasceu:')
nome = str(input('\033[1;36mNOME:')).strip().upper()
print('\033[0;30m[ 1 ] = Se você é homem\n'
      '[ 2 ] = Se você é mulher')
sexo = int(input('\033[1;36mQual é o seu sexo(1 ou 2):'))
ano = int(input('ANO EM QUE NASCEU:'))
ant = date.today().year
idade = ant - ano
print('')
print('\033[4;30mANALIZANDO...')
sleep(1)
print('\033[46m{}\033[m'.format('  ' * 40))
if sexo == 2:
    print('\033[1;30mVocê não é obrigada a se alistar.')
    print('Você gostaria de se alistar nas Forças Armadas?\n\033[0;30m'
          '[ 1 ] = SIM\n'
          '[ 2 ] = NÃO')
    sxn = int(input('\033[1;36mEscolha 1(SIM) ou 2(NÃO):'))
    if sxn == 2:
        print('\033[1;30mEntendi,tenha um ótimo dia!')
    elif sxn == 1:
        print('\033[1;30mVamos verificar sua idade...')
        sleep(1)
        print('\033[46m{}\033[m'.format('  ' * 40))
        if idade >= 18:
            print('\033[1;30mVocê já pode se alistar no exercito,\n'
                  'vá na junta militar de sua cidade e se aliste!')
        else:
            print('\033[1;30mVocê só pode se alistar daqui {} anos, em {}.'.format(18 - idade, 18 + ano))
    else:
        print('\033[4;31mERROR:DIGITE 1 OU 2.')
elif sexo == 1:
    if idade > 18:
        print('\033[1;30mVocê já deveria ter se alistado há {} anos.'
              '\n\033[0;30mSe você ainda não passou no alistamento,'
              '\nvá a junta militar de sua cidade e se aliste,'
              '\ne você deverá pagar uma multa pelo seu atraso,'
              '\npois seu alistamento foi em {}.'.format(idade - 18, ant - (idade - 18)))
    elif idade < 18:
        print('\033[1;30mVocê deverá se alistar daqui {} anos.'
              '\n\033[0;30mOu seja, em {}, você deverá ir para a'
              '\njunta militar de sua cidade e se alistar'.format(18 - idade, 18 + ano))
    elif idade == 18:
        print('\033[1;30mVocê deverá se alistar nesse ano!'
              '\n\033[0;30mVá para a junta militar de sua cidade'
              '\ne se aliste!Porque {} é o seu ano!!!'.format(ant))
else:
    print('\033[4;31mERROR:DIGITE 1 OU 2.Para dizer se você é homem ou mulher.')
print('\033[1;30mMuito obrigado por sua atenção,{}.'.format(nome))
print('\033[46m{}\033[m'.format('  ' * 40))
