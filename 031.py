distancia = float(input('A distância em quilômetros'))
if distancia <=200:
    preco_passagem=distancia*0.5
else:
    preco_passagem=distancia*0.45

preco_passagem2 = distancia * 0.5 if distancia <=200 else distancia * 0.45
print('{:.2f}'.format(preco_passagem2))

print('O valor da passagem é \033[35m R${:.2f}'.format(preco_passagem))
