from math import sqrt
import emoji

num = int(input('digite um numero: ' + emoji.emojize(':earth_americas:', use_aliases=True)))
sqrt = sqrt(num)
print('A Raíz de {} é {:.2f}'.format(num, sqrt))
