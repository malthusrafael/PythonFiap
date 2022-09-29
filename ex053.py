numeros = []
for i in range(1, 21, 1):
    n1 = int(input('Digite um numero: '))
    numeros.append(n1)
const = int(input('Digite um valor para a constante: '))
for i in range(0, 20, 1):
    numeros[i] = numeros[i]*const
for it in numeros:
    print(numeros[i])