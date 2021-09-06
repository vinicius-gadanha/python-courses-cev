from datetime import date
nome = str(input('\033[1;36mDigite seu nome:')).strip().upper()
ano = int(input('Digite seu ano de nascimento:'))
ant = date.today().year
idade = ant - ano
print('')
print('\033[46m{}\033[m'.format('  ' * 30))
print('\033[1;30mO atleta {}, tem {} anos.'.format(nome, idade))
if idade <= 9:
    print('CLASSIFICAÇÃO:MIRIM')
elif 9 < idade <= 14:
    print('CLASSIFICAÇÃO:INFANTIL')
elif 14 < idade <= 19:
    print('CLASSIFICAÇÃO:JUNIOR')
elif 19 < idade <= 25:
    print('CLASSIFICAÇÃO:SÊNIOR')
elif 25 < idade:
    print('CLASSIFICAÇÃO:MESTRE')
print('\033[46m{}\033[m'.format('  ' * 30))
