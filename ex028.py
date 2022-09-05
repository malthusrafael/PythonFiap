#28. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente.
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero:'))
n3 = float(input('Digite o terceiro numero: '))
l = [n1,n2,n3]
print(sorted(l))