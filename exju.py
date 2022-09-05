char = '_'
print(char*70)
print(char * 30, 'OPERAÇOES', char * 29)
print(f'{char * 30} 1.MULTIPLICAÇÃO {char * 23}')
print(f'{char * 30} 2.ADIÇAO  {char * 29}')
print(f'{char * 30} 3.DIVISÃO {char * 29}')
print(f'{char * 30} 4.SUBTRAÇÃO {char * 27}')
print(f'{char:<30} 5.SAIR {char:>32}')
print(char * 70)
op = int(input('Digite a operaçao desejada 1,2,3,4 ou 5 Para sair: '))

if (op == 1):
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o segundo número: "))
    r = v1 * v2
    print(f"O resultado é: {r}")

elif (op == 2):
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o segundo número: "))
    r = v1 + v2
    print(f"O resultado é: {r}")

elif (op == 4):
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o segundo número: "))
    r = v1 - v2
    print(f"O resultado é: {r}")

elif (op == 3):
    v1 = float(input("Digite o primeiro número: "))
    if (v1 == 0):
        print("O denominador deve ser diferente de zero")
    else:
        v2 = float(input("Digite o segundo número: "))
        r = v1 / v2
        print(f"O resultado é: {r}")

elif (op == 5):

    print("Fim do processo, até logo!")

else:
    print('Ops! opção inexistente!')