#32. Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro.
# Caso contrário solicitar novamente apenas o segundo valor.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while n2 <= n1:
    n2 = float(input(f'O segundo valor deve ser maior que o primeiro que foi ({n1}). Digite o segundo valor: '))
print(f'O primeiro valor é ({n1}), e o segundo,que é maior, é ({n2}) ')