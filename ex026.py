#26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
# imprimindo o resultado.
n1 = int(input('Digite um numero: '))
if n1 < 0:
    n2 = n1*3
    print(f'O numero {n1} é negativo e seu triplo é {n2}')
else:
    n3 = n1*2
    print(f'O numero {n1} é positivo e seu dobro é {n3}')