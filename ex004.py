n = input('digite algo')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alphanumerico? {}'.format(n.isalnum()))
print('Está em maiúsculas?{}'.format(n.isupper()))
print('Está em minúsculas?{}'.format(n.islower()))
print('Está capitalizado?{}'.format(n.istitle()))
