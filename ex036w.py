# caso contrário, digitar novamente somente o segundo. Após a validação dos dados,
# exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.
n1 = int(input('Digite um numero positivo para saber sua tabuada : '))
while (n1 <= 0):
    print('Nao pode ser negativo!')
    n1 = int(input('Digite um numero positivo para saber sua tabuada: '))

a = int(input('Digite o primeiro numero do intervalo que deseja calcular: '))
b = int(input('Digite o segundo numero do intervalo que deseja calcular: '))
while b <= a:
    print('O segundo numero deve ser maior que o primeiro! ')
    b = int(input('Digite o segundo numero do intervalo que deseja calcular: '))

while b >= a:
    r = n1*b
    print(f'{n1} X {b}  = {r}')
    b = b-1