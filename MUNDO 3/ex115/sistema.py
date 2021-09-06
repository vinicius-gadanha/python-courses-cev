from time import sleep
from ex115.lib import menu, arquivo

arq = 'cursoemvideo.txt'

if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)

while True:
    menu.menu()
    opc = menu.escolha('\033[1;32mSua Opção: \033[m')

    if opc == 1:
        menu.formato('PESSOAS CADASTRADAS')
        arquivo.lerarquivo(arq)
        sleep(1)

    elif opc == 2:
        menu.formato('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = menu.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
        sleep(1)

    elif opc == 3:
        menu.formato('Saindo do sistema... Até logo!')
        break
