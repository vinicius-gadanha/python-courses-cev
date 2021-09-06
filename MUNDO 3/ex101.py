def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        vt = f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        vt = f'Com {idade} anos: É OPCIONAL.'
    else:
        vt = f'Com {idade} anos: É OBRIGATÓRIO.'
    return vt


# Programa Principal
print('=' * 30)
n = int(input('Em que ano você nasceu: '))
print(voto(n))
print('=' * 30)
