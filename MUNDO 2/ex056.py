muie = 0
macho = 0
maior = 0
pess = 0
soma = 0
for pess in range(1, 5):
    print('\033[1;30m{} {}ª PESSOA {}'.format('-' * 7, pess, '-' * 7))
    nome = str(input('Nome:')).strip().capitalize()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).upper().strip()
    soma += idade
    if pess == 1 and sexo == 'M':
        maior = idade
        macho = nome
    if idade > maior and sexo == 'M':
        maior = idade
        macho = nome
    if idade < 20 and sexo == 'F':
        muie += 1
print('\n\033[1;36mA média de idade do grupo é de {:.1f} anos.'.format(soma / pess))
if maior > 0:
    print('O homem mais velho tem {} anos e se chama {}.'.format(maior, macho))
else:
    print('Na lista não há homens!')
if muie > 1:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(muie))
elif muie == 1:
    print('Só tem uma mulher com menos de 20 anos.')
else:
    print('Não tem nenhuma mulher com menos de 20 anos.')
