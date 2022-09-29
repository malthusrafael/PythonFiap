#35. Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar somente valores positivos.
# Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um a dez.

n1 = int(input('Digite um numero positivo para saber sua tabuada: '))
while (n1 <= 0):
    print('Nao pode ser negativo!')
    n1 = int(input('Digite um numero positivo para saber sua tabuada: '))
i = 1
while i<11:
    r = n1*i
    print(f'{n1} X {i} = {r}')
    i = i + 1