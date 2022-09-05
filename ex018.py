#18. Criar um programa para analisar a velocidade de um automóvel.
# Solicitar via teclado os valores da aceleração (a em m/s2),
# velocidade inicial (v0 em m/s) e o tempo de percurso (t em s).
# Calcular e exibir a velocidade final do automóvel em km/h. E exibir mensagem de acordo com a tabela abaixo:
a  = float(input('Digite a aceleraçao m/s2: '))
t =  float(input('Digite o tempo (s): '))
v = float(input('Digite a velocidade (m/s): '))

vf = v+a*t
c = vf*3.6

if c <= 40:
    print(f'Veiculo esta a {c:.2f}, muito lento!')
elif 40 < c and c<= 60:
    print(f'Veiculo esta a {c:.2f}, Velocidade permitida!')
elif 60 < c and c <=80:
    print(f'Veiculo esta a {c:.2f}, velocidade de cruzeiro')
elif 80< c and c <= 120:
    print(f'veiculo esta a {c:.2f}, veiculo esta rapido!')
else:
    print(f'veiculo esta a {c:.2f}, muito Rapido!')