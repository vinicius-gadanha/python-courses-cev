from datetime import date

pessoa = {'NOME': str(input('Nome: ')).capitalize().strip(),
          'IDADE': date.today().year - (int(input('Ano de Nascimento: '))),
          'CTPS': int(input('Carteira de Trabalho (Digite "0" se você não tem): '))}
if pessoa['CTPS'] > 0:
    pessoa['CONTRATAÇÃO'] = int(input('Ano de contratação: '))
    pessoa['SALÁRIO'] = float(input('Salário: R$'))
    pessoa['APOSENTADORIA'] = 35 - (date.today().year - pessoa['CONTRATAÇÃO']) + pessoa['IDADE']

print('=' * 30)
for k, v in pessoa.items():
    print(f'{k}: {v}')
print('=' * 30)
