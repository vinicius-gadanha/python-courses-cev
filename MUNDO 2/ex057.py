sexo = str(input('Digite seu sexo (MACULINO[M] ou FEMININO[F]):')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos.Por favor informe seu sexo:')).strip().upper()[0]
if sexo == 'F':
    sexo = 'Feminino'
elif sexo == 'M':
    sexo = 'Masculino'
print('Sexo {} registrado com sucesso!!!'.format(sexo))
