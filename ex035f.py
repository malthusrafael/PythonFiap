#35. Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar somente valores positivos.
# Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um a dez.
n = int(input('Digite o valor a ser multiplicado: '))

while (n < 0):
    n = int(input('Valores negativos não são permitidos.\nDigite novamente: '))

i = 1

for i in range(1, 11, 1):
    r = n * i
    print(f'{n} X {i} = {r}')