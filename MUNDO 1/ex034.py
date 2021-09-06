from termcolor import colored
sal = float(input(colored('Qual é o salário do funcionário? R$', 'blue')))
if sal > 1250:
    aum = sal * (10/100)
else:
    aum = sal * (15/100)
print(colored('$'*60, 'yellow'))
print(colored('O valor de seu aumento é de {:.2f} reais.', 'red').format(aum))
print(colored('Ou seja,o valor total do novo salário será de {} reais', 'red').format(sal+aum))
print(colored('$'*60, 'yellow'))
