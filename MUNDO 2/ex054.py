from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    idade = int(input('Em que ano a {}ª pessoa nasceu?'.format(c)))
    if date.today().year - idade >= 21:
        maiores += 1
    else:
        menores += 1
print('''Ao todo tivemos {} arquivo maiores de idade.
E também tivemos {} arquivo menos de idade'''.format(maiores, menores))
