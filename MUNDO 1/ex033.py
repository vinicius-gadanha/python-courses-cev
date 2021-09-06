from termcolor import colored

print(colored('DIGITE TRÊS NÚMEROS DIFERENTES', 'yellow'))
n1 = int(input(colored('Primeiro número:', 'blue')))
n2 = int(input(colored('Segundo número:', 'blue')))
n3 = int(input(colored('Terceiro número:', 'blue')))
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(colored('-=-' * 10, 'yellow'))
print(colored('O número maior é o {}.', 'cyan').format(maior))
print(colored('O número menor é o {}.', 'red').format(menor))
print(colored('-=-' * 10, 'yellow'))
