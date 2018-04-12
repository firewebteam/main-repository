print('Obliczę dla ciebie miejsca zerowe funkcji f(x)=ax^2+bx+c i podam jej wierzchołek:)')
a = float(input('Podaj liczbe całkowitą a:'))
if a == 0:
    print('Gdy a=0 nie otrzymamy funkcji kwadratowej, a funkcję liniową f(x)=bx+c.')
    print('Ale z nią też sobie poradzimy:D')
    b = float(input('Podaj liczbe całkowitą b:'))
    if b == 0:
        print('Gdy b=0 nie otrzymamy funkcji liniowej, a funkcję stałą f(x)=c.')
        c = float(input('Podaj liczbe całkowitą c:'))
        if c == 0:
            print('Podana przez ciebie funkcja to f(x)=0. Ma ona nieskończoną liczbę miejsc zerowych.')
        else:
            print('Podana przez ciebie funkcja to f(x)=%.0f. Nie ma ona miejsc zerowych.' % c)
    else:
        c = float(input('Podaj liczbe całkowitą c:'))
        print('Miejsce zerowe funkcji f(x)=%.0fx+%.0f to x=%.2f' % (b, c, c / b))
    print('Funkcje liniowe nie mają wierzchołków.')
else:
    b = float(input('Podaj liczbe całkowitą b:'))
    c = float(input('Podaj liczbe całkowitą c:'))
    d = (b ** 2) - 4 * a * c
    print('Delta wynosi %.2f.' % d)
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