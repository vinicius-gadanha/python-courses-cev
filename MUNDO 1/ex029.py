#import random
#v = random.randint(0, 200)
from termcolor import colored
nome = str(input(colored('Digite seu nome:', 'blue'))).strip().upper()
v = int(input(colored('Em que velocidade seu carro estava?', 'blue')))
print(colored('Bom dia {}.\nA velocidade do seu carro era de {}km/h.', 'yellow').format(nome, v))
if v >= 80:
    print(colored('Ou seja você se fudeu, e vai se multado.', 'red'))
    print(colored('Preço a pagar: {:.2f} reais', 'red').format(float((v - 80)*7.00)))
else:
    print(colored('Parabéns, sua velocidade está abaixo do limite.', 'green'))
    print(colored('Ou seja, você não tem multa para pagar.', 'green'))
