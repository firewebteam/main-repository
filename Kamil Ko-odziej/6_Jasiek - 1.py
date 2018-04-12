t = int(input('Podaj sekundę ruchu Jaśka:'))
if t > 100:
    print('Jasiek przeszedł już całe 380 metrów')
elif t < 0:
    print('Jasiek jeszcze nie zaczął się poruszać')
else:
    print('Jasiek przeszedł %.2f metrów' % (t*3.8))