#23. Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if a+b < c:
    print(f'A soma de A {a} + B {b} é menor do que C {c}')
elif a+b == c:
    print(f'A soma de A {a} + B {b} é igual a C {c}')
else:
    print(f'A soma de A{a} + B{b} é maior do que C {c}')
