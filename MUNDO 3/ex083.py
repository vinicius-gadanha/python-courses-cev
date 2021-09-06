lista = []
expr = str(input('Digite a expressão: ')).strip()
for c in range(0, len(expr)):
    lista.append(expr[c])
if lista.count('(') == lista.count(')') and lista.index('(') < lista.index(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
