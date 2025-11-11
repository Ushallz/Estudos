from math import(sin, cos, tan, radians)
angle=float(input('digite um número(ângulo)'))
rad=radians(angle)
print('o seno de {} é {:.1f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angle,sin(rad),cos(rad),tan(rad)))