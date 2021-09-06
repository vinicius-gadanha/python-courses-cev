c = str(input('\033[1;30mDigite o nome de uma cidade:'))
x = c.capitalize().strip().split()
y = 'Santo' in x[0]
print('-'*50)
print('Essa cidade começa com a palavra Santo? {}'.format(y))
print('-'*50)
print('OBS: Se apareceu TRUE quer dizer que sim\n     Se apareceu FALSE quer dizer que não')
print('-'*50)
