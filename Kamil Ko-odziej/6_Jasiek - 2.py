v = ((3 ** 2) + (2 ** 2)) ** (1 / 2)
t = int(input('Podaj sekundę ruchu Jaśka:'))
if t > 100:
    print('Jasiek przeszedł już całe %.3f metrów' % (100*v))
elif t < 0:
    print('Jasiek jeszcze nie zaczął się poruszać')
else:
    print('Jasiek przeszedł %.3f metrów' % (t*v))