palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    x = str(palavras[c])
    print('\033[1;30m\nNa palavras {} temos: \033[1;31m'.format((palavras[c]).upper()), end='')
    for n in range(0, len(x)):
        if x[n] == 'a':
            print('a', end=' ')
        elif x[n] == 'e':
            print('e', end=' ')
        elif x[n] == 'i':
            print('i', end=' ')
        elif x[n] == 'o':
            print('o', end=' ')
        elif x[n] == 'u':
            print('u', end=' ')
