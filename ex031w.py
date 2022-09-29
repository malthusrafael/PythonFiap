#31. Criar uma rotina de entrada que aceite somente um valor positivo.
n1 = int(input('Digite um valor positivo: '))
while n1 <= 0:
    print('Não pode ser negativo!')
    n1 = int(input('Digite um valor positivo'))