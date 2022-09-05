#21. Entrar via teclado com dois valores quaisquer. Após a digitação,
# exibir um seletor de opções (“menu”) com as seguintes opções: (Fazer esse exercício utilizando If..Else e/ou Case)

#1 – Multiplicação
#2 – Adição
#3 – Divisão
#4 – Subtração
#5 – Fim de processo (sair do programa)

#Solicitar uma opção por parte do usuário, verificar se é ou não uma opção válida (letras ou números)
# e processar a respectiva operação. Enviar mensagem de erro se a opção escolhida não existir no seletor.

#Encerrar o programa somente quando o usuário escolher a opção de finalização.
# Repare que a opção de número três é de divisão e o programa deverá enviar mensagem de erro,
# (somente nesta opção) se o denominador for zero.

char = '*'
print(char * 30, 'OPERAÇOES', char * 29)
print(f'{char:<30} 1.MULTIPLICAÇÃO {char:>23}')
print(f'{char:<30} 2.ADIÇAO  {char:>29}')
print(f'{char:<30} 3.DIVISÃO {char:>29}')
print(f'{char:<30} 4.SUBTRAÇÃO {char:>27}')
print(f'{char:<30} 5.SAIR {char:>32}')
print(char*70)
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

elif (op == 3):
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o segundo número: "))
    r = v1 / v2
    print(f"O resultado é: {r}")

elif (op == 4):
    v1 = float(input("Digite o primeiro número: "))
    if (v1 == 0):
        print("O denominador deve ser diferente de zero")
    else:
        v2 = float(input("Digite o segundo número: "))
        r = v1 - v2
        print(f"O resultado é: {r}")

elif (op == 5):

    print("Fim do processo!")

else:
    print('Opção inexistente, tente novamente!')