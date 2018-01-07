t = int(input('Podaj sekundę ruchu Jaśka:'))
if t > 100:
    t = 100
    x = complex(3 * t, 2 * t)
    print('Jasiek przeszedł już całe %.4f metrów' % (abs(x)))
elif t < 0:
    print('Jasiek jeszcze nie zaczął się poruszać')
else:
    x = complex(3 * t, 2 * t)
    print('Jasiek przeszedł %.3f metrów' % (abs(x)))