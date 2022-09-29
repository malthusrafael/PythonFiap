#40. Exibir os vinte primeiros valores da série de Bergamaschi. A série: 1, 1, 1, 3, 5, 9, 17, …
a = 1
b = 1
c = 1
i = 1

while (i <= 20):
    print(a)
    s = b + a + c
    a = b
    b = c
    c = s
    i = i + 1