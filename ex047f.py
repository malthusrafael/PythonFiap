# 47. Calcular o fatorial de um valor que será digitado. Este valor não poderá ser negativo.
# Enviar mensagem de erro e solicitar o valor novamente, se necessário.
# Perguntar se o usuário deseja ou não fazer um novo cálculo, consistir a resposta em “S” ou “N”.
# N! = N x N-1 x N-2 x N-3 x ....... x (N - (N-1))
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

r = ()
while(r!="N"):
    n = int(input("Digite um valor positivo: "))
    while(n < 0):
        print("Valor invalido!")
        n = int(input("Digite um valor positivo: "))
    for i in range(n,0,-1):
        if(i == n):
            f = i
        else:
            f = f * i
    print(f"{n}!={f}")
    r = input("Deseja uma nova execução? (S) ou (N):")
    while((r!="S")and (r!="N")):
        print("Invalido! Apenas (S) ou (N).")
        r = input("Deseja uma nova execução? (S) ou (N):")