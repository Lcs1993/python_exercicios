print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel\033[32m formar um triângulo')
else:
    print('\033[31m Não é possivel\033[m formar um triângulo')
