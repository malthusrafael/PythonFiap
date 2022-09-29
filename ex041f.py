#41. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo.
# O valor “N” será digitado, deverá ser positivo, mas menor que cem.
# Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
#A seqüência: 2, 5, 10, 17, 26, ....
n = int(input('Digite o valor a ser somado: '))

while (n < 0) or (n > 100):
    n = int(input('O valor precisa ser positivo e menor que 100.\nDigite novamente: '))

for i in range(0, n, 1):
    if (i==0):
        a=((i + 1) * (i + 1)) + 1
    else:
        a = a + ((i + 1) * (i + 1)) + 1
        print(a)