#5. Entrar via teclado com o valor de uma temperatura em graus Celsius,
#calcular e exibir sua temperatura equivalente em Fahrenheit
c = float(input('Digite a temperatura em Celsius para saber a temperatura equivalente em Fahrenheit: '))
f = (c*9/5)+32
print(f'A temperatura de {c}°C equivale a {f}°F')