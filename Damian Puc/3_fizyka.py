i="tak"
while i=="tak":
    t = float(input("Wprowadz czas: "))

    if t>100:
        print("Jasiek przeszedl cala droge.")
        print("Droga w poziomie = ", 3 * 100)
        print("Drpga w pionie = ", 2 * 100)
        print("Droga w lini prostej = ", abs(complex(3*100,2*100)))
        i = input("Czy chsesz dalej wpisywac czas?: ")
    else:
        print("Jasiek przeszedl: ")
        print("Droga w poziomie = ", 3 *t)
        print("Drpga w pionie = ", 2 * t)
        print("Droga w lini prostej = ", abs(complex(3 * t, 2 * t)))
        i = input("Czy chsesz dalej wpisywac czas?: ")