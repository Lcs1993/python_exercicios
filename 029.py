
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade >80:
    print('\033[31m MULTADO! \033[m você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) *7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia!Dirija com segurança!')
