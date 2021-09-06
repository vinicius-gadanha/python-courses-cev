palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\033[1;30m\nNa palavra {p.upper()} temos: \033[1;31m', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
