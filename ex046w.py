# 46. Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado,
# deverá ser positivo, mas menor que vinte. Caso a quantidade não satisfaça a restrição,
# enviar mensagem de erro e solicitar o valor novamente. Após a digitação dos “N” valores, exibir:
# a) O maior valor;
# b) O menor valor;
# c) A soma dos valores;
# d) A média aritmética dos valores;
# e) A porcentagem de valores que são positivos;
# f) A porcentagem de valores negativos;
# Após exibir os dados, perguntar ao usuário se deseja ou não uma nova execução do programa.
# Consistir a resposta no sentido de aceitar somente “S” ou “N” e encerrar o programa em função dessa resposta.
r = ()
while (r != "N"):
    p = 0
    p2 = 0

    n = int(input("Digite quantos valores(positivos e menor que 20) seram solicitados: "))
    while (n <= 0 or n >= 20):
        print("Valor invalido!")
        n = int(input("Digite um valor positivo menor que 20: "))
    i = 1
    while (i <= n):
        num = int(input(f"Digite um valor(n{i}) : "))

        if (i == 1):
            a = num
        elif (num > a):
            a = num

        if (i == 1):
            b = num
        else:
            b = b + num

        if (i == 1):
            c = num
        elif (num < c):
            c = num

        if (num > 0):
            p = p + 1
        x = (p * 100) / n

        if (num < 0):
            p2 = p2 + 1
        x2 = (p2 * 100) / n
        i = i + 1
    print("O maior valor é:", a, "\nO menor valor é:", c, "\nA soma dos valores é:", b, "\nA media aritimetica é:",
          b / 10, "\nPorcentagem de valores positivos é:", x, "\nPorcentagem de valores negativos:", x2)
    r = input("Deseja uma nova execução? (S) ou (N):")
    while ((r != "S") and (r != "N")):
        print("Invalido! Apenas (S) ou (N).")
        r = input("Deseja uma nova execução? (S) ou (N):")