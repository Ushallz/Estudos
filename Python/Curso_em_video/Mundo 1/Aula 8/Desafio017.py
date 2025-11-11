import math
a=float(input('Digite o comprimento do cateto oposto'))
b=float(input('Digite o comprimento do cateto adjacente'))
c=math.hypot(a, b)
print('o comprimento da hipotenusa será igual a {:.2f}'.format(c))
