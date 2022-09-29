#38. Exibir a soma dos números inteiros positivos do intervalo de um a cem.
n = 0
for i in range(1, 101, 1):
    n = n + i
print('A soma de 1 a 100 é: ', n)