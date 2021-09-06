c = float(input('\033[1;36mInforme a temperatura em °C:'))
f = (c * 9 / 5) + 32
k = c + 273
print('\033[1;30m-'*30)
print('   Celsius: {:.1f}°C'.format(c))
print('Fahrenheit: {:.1f}°F'.format(f))
print('    Kelvin: {:.1f}°K'.format(k))
print('-'*30)
