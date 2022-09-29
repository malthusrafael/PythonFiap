# caso contrário, digitar novamente somente o segundo. Após a validação dos dados,
# exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.

n = int(input('Digite o valor a ser multiplicado: '))

while (n < 0):
    print('Números negativos não são permitidos.')
    n = int(input('Por favor, digite novamente: '))

a = int(input('Digite o primeiro numero do intervalo que deseja calcular: '))

b = int(input('Digite o segundo numero do intervalo que deseja calcular: '))

while (a > b):
    b = int(input('O segundo valor precisa ser maior que o primeiro.\nDigite novamente: '))

for i in range(b, a-1, -1):
    r = n * i
    print(f'{n} X {i} = {r}')
