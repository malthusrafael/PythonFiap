# 50. Elabore um programa que apresente os números pares maiores que 10 no intervalo fechado [A, B].
# Sendo que A e B serão números inteiros escolhidos pelo usuário.
# Um número é par quando este satisfaz a seguinte condição: (NÚMERO mod 2 = 0)

inteiro = int(input('Digite o intervalo que será solicitado dos valores: '))
n = 1
p = 0
i = 0

while (n <= inteiro):
    a = int(input('Digite o valor: '))
    while (a < 10):
        print('O valor deve ser maior que 10.')
        a = int(input('Digite o valor: '))
    n = n + 1
    if (a % 2 == 0):
        a = p
        p = p + 1
    else:
        a = i
        i = i + 1

print('A quantidade de números pares é: ', p)
print('A quantidade de números ímpares é: ', i)