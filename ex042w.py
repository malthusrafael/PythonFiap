##42. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo.
# O valor “N” será digitado, deverá ser positivo, mas menor que cinqüenta.
# Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente.
a = 1
b = 2
x = a / b

n = int(input("Digite um valor positivo menor que 50: "))

while(n <= 0 or n > 50):
    print("Valor invalido!")
    n = int(input("Digite um valor positivo menor que 50: "))
i = 1
while(i <= n):
    a = a + 1
    b = b + 1
    x = x + (a/b)
    print(f"O {i}º valor é:",x)
    i = i + 1