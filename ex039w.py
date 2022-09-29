#39. Exibir os trinta primeiros valores da série de Fibonacci. A série: 1, 1, 2, 3, 5, 8, ...

print('Sequencia Fibonacci')
n1 = 0
print(n1)
n2 = 1
print(n2)
c = 1
while c<31:
    c =c+1
    n3 = n1+n2
    print(n3)
    n1 = n2
    n2 = n3