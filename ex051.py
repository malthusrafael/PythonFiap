#armazenar dez numeros na memória do computador.Exibir os valores na ordem inversa a da digitaçao
numeros = []

for i in range(0, 10, 1):
    n1 = int(input('Digite um numero: '))
    numeros.append(n1)
for i in range(9, -1, -1):
    print(numeros[i])