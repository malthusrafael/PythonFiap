# 47. Calcular o fatorial de um valor que será digitado. Este valor não poderá ser negativo.
# Enviar mensagem de erro e solicitar o valor novamente, se necessário.
# Perguntar se o usuário deseja ou não fazer um novo cálculo, consistir a resposta em “S” ou “N”.
# N! = N x N-1 x N-2 x N-3 x ....... x (N - (N-1))
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
resposta = 'S'

while (resposta == 'S'):

    num = int(input('Deseja calcular o fatorial de qual número? '))

    while (num <= 0):
        print('Opa! Não pode número negativo!')
        num = int(input('Deseja calcular o fatorial de qual número? '))

    for i in range(num - 1, 0, -1):
        resultado = num * i
        num = resultado

    print('Fatorial: ', resultado)
    resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()

    while (resposta != 'S' and resposta != 'N'):
        print('Seguir padrão de resposta S/N')
        resposta = input('Deseja uma nova execução do programa?(S/N) ').upper()

        r = input("Deseja uma nova execução? (S) ou (N):")