from termcolor import colored

print(colored('=' * 55, 'yellow'))
print(colored('ANALIZADOR DE TRIÂNGULOS:', 'yellow'))
print(colored('=' * 55, 'yellow'))
print(colored('DIGITE O COMPRIMENTO PARA TRÊS RETAS', 'cyan'))
r1 = float(input(colored('Primeira reta:', 'blue')))
r2 = float(input(colored('Segunda reta:', 'blue')))
r3 = float(input(colored('Terceira reta:', 'blue')))
maior = r1
menor = r2 + r3
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('podem formar um triangulo')
# else:
#    print('nao podem formar um triangulo')
if r2 > r1 and r2 > r3:
    maior = r2
    menor = r1 + r3
if r3 > r1 and r3 > r2:
    maior = r3
    menor = r1 + r2
print(colored('=' * 55, 'yellow'))
if menor > maior:
    print(colored('Com essas três retas É POSSIVEL criar um triângulo.', 'yellow'))
else:
    print(colored('Com essas três retas NÃO É POSSIVEL criar um triângulo.', 'red'))
print(colored('=' * 55, 'yellow'))
