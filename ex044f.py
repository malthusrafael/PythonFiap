#44. Entrar via teclado com dez valores positivos.
# Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
#a) O maior valor;
#b) A soma dos valores;
#c) A média aritmética dos valores;
s = 0

for i in range(1, 11, 1):
    n = int(input('Digite um valor: '))

    if (i == 1):
        m = n
    elif(n > m):
        m = n

    s = s + n

md = s / 10

print('O maior valor é ', m)
print('A soma é ', s)
print('A média é ', md)