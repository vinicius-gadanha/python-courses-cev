from termcolor import colored
# ult = num % 2
num = str(input(colored('Digite um número inteiro:', 'green'))).strip()
par = str(20468)
ult = (num[len(num) - 1])
vdd = ult in par
print(colored('-', 'yellow') * 50)
if vdd:
    print(colored('O número {} é considerado um número par.', 'blue').format(num))
else:
    print(colored('O número {} é considerado um número ímpar.', 'red').format(num))
print(colored('-', 'yellow') * 50)
