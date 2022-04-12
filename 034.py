salário = float(input('Qual é o salário do funcionário?'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo =  salário + (salário * 10/100)
print('Quem ganhava R${:.2f} \033[32m passa a ganhar R${:.2f} \033[m agora'.format(salário, novo))
