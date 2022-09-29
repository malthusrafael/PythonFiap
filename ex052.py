# 52 Armazenar dez valores na memória do computador. Após a digitaçao dos valores,
# criar uma rotina para ler os valores e achar e exibir o maior deles.

numeros = []
for i in range(0, 10, 1):
    n1 = int(input('Digite um numero: '))
    numeros.append(n1)
m = numeros[0]
for i in range(0, 10, 1):
    if (numeros[i]> m):
        m = numeros[i]
print(f'O maior valor é {m}')
