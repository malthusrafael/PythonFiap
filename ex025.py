#25. Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.
# Utilize o operador %
n1 = float(input('Digite um numero qualquer para informar se ele é par ou impar: '))
if n1 % 2 == 0:
    print('numero par')
else:
    print('numero impar')