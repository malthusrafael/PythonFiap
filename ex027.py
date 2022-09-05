#27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar,
# imprimir o resultado desta operação.
n1 = float(input('Digite um numero e some 5 caso seja par ou some 8 caso seja ímpar: '))
if n1 % 2 == 0:
    n2 = n1 +5
    print(f'O numero {n1} é par, somando 5 temos {n2}')
else:
    n3 = n1+8
    print(f'numero {n1} é impar, somando 8 temos {n3}')