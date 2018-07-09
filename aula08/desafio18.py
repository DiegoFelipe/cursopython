from math import sin, radians, cos, tan

an = float(input('digite o angulo'))
seno = sin(radians(an))
print('o ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('o ângulo de {} tem o tangente de {:.2f}'.format(an, tan))
