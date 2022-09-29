# 48. Crie um programa em que o usuário entre com um número inteiro qualquer,
# e o programa imprima os 20 números subsequentes ao que foi digitado pelo usuário

n = int(input('Digite um valor qualquer: '))
t = n + 20

i = n

while(n < t):
    n = i + 1
    print(n)
    i = i + 1