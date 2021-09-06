def notas(num, sit=False):
    """
    =>Função para analizar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos(aceita várias)
    :param sit: valor opcional, indicando se deve ou nçao adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    inf = {'Nº TOTAL DE NOTAS': len(num),
           'MAIOR NOTA DA SALA': max(num),
           'MENOR NOTA DA SALA': min(num),
           'MÉDIA DA SALA': sum(num) / len(num)}
    if sit:
        if sum(num) / len(num) >= 7:
            inf['SITUAÇÃO DA SALA'] = 'BOA'
        elif 5 <= sum(num) / len(num) < 7:
            inf['SITUAÇÃO DA SALA'] = 'RAZOÁVEL'
        else:
            inf['SITUAÇÃO DA SALA'] = 'RUIM'
    print('=' * 30)
    return inf


lista = []
c = 1
while True:
    print('=' * 30)
    no = float(input(f'{c}º NOTA: '))
    lista.append(no)
    son = str(input('Quer continuar??[S/N]: ')).strip().upper()[0]
    while son not in 'SN':
        son = str(input('Quer continuar??[S/N]: ')).strip().upper()[0]
    if son == 'N':
        break
    c += 1

resp = notas(lista, sit=True)
for k, v in resp.items():
    print(f'{k:>20}: {v}')
print('=' * 70)
help(notas)
print('=' * 70)
