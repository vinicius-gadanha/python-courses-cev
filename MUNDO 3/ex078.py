valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=' * 50)
print(f'Você digitou os valores: {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
