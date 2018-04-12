a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))
c = int(input("Podaj liczbę c:"))
if a == 0 and b == 0 and c == 0:
    print("funkcja f(x)=0 ma nieskończoną liczbę mniejsc zerowych")
elif a == 0 and b == 0:
    print("Funkcja f(x)=%d nie ma miejsc zerowych." % c)
elif a == 0:
    print('Miejsce zerowe funkcji f(x)=%dx+%d to x=%.2f.'%(b,c,c / b))
else:
    d = (b ** 2) - 4 * a * c
    if d >= 0:
        x1 = float((-b - d ** (1 / 2)) / 2 * a)
        x2 = float((-b + d ** (1 / 2)) / 2 * a)
    p = float(-b / 2 * a)
    q = float(-d / 4 * a)
    if d > 0:
        print('Miejsca zerowe funkcji f(x)=%.0fx^2+%.0fx+%.0f to %.2f i %.2f.' % (a, b, c, x1, x2))
    elif d == 0:
        print('Miejsce zerowe funkcji f(x)=%.0fx^2+%.0fx+%.0f to:%.2f' % (a, b, c, x2))
    else:
        print('Delta jest ujemna więc funkcja f(x)=%.0fx^2+%.0fx+%.0f nie ma pierwiastków rzeczywistych.' % (a, b, c))
    print('Wierzchołek funkcji ma współrzędne P=(%.2f,%.2f).' % (p, q))
