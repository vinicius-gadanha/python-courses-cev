nome = str(input('\033[1;30mDigite seu nome completo:')).strip().split()
print('\033[1;31m-' * 70)
print('\033[4;30mAnalizando esse nome: {}'.format(' '.join(nome).upper()))
print('\033[1;31m-' * 70)
print('\033[4;30mPrimeiro nome:     {:3}'.format(nome[0].title()))
print('\033[4;30mÚltimo sobrenome:  {}'.format(nome[len(nome) - 1].title()))
print('\033[1;31m-' * 70)

# xone = str('-'.join(nome))
# yone = str(xone).rfind('-')
# zone = yone + 1
# aone = xone[zone:]
