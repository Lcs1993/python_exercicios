from math import sin,tan,cos,radians
n = int(input('Digite um ângulo'))
n = radians(n)
seno = sin(n)
print('O valor do seno é {:.2f}'.format(seno))
tang = tan(n)
print ('O valor do tangente é {:.2f}'.format(tang))
cos = cos(n)
print('O valor do cosseno é {:.2f}'.format(cos))

