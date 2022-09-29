# 49. Crie um programa que solicite que o usuário entre com dois números (inicial e final).
# Ao final o programa deverá apresentar o valor total da soma de todos os números do intervalo digitado pelo usuário.

inicial = int(input('Digite o valor inicial: '))

final = int(input('Digite o valor final: '))

s = 0
i = 1

while (inicial <= final):
    s = s + inicial
    inicial = inicial + 1
print(s)