num = int(input('\033[1;36mDigite um número inteiro:'))
print('\033[1;30mEscolha uma das bases para conversão:')
print('\033[40m{}\033[m'.format('  ' * 30))
print('\033[1;30m[ 1 ] = converter para Binário\n[ 2 ] = converter para OCTAL\n[ 3 ] = converter para HEXADECIMAL')
print('\033[40m{}\033[m'.format('  ' * 30))
esc = int(input('\033[1;30mSua opção:'))
print('\033[40m{}\033[m'.format('  ' * 30))
if esc == 1:
    print('\033[1;30m{}\033[30m convertido para BINÁRIO é igual a \033[1;30m{}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('\033[1;30m{}\033[30m convertido para OCTAL é igual a \033[1;30m{}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('\033[1;30m{}\033[30m convertido para HEXADECIMAL é igual a \033[1;30m{}'.format(num, hex(num)[2:]))
else:
    print('\033[4;31mERRO:OPÇÃO INVALIDA.Tente novamente, muito obrigado por sua atenção!')
print('\033[40m{}\033[m'.format('  ' * 30))
