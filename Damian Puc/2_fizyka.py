v = 3.8

i="tak"
while i=="tak":
    t = float(input("Wprowadz czas: "))
    if t>100:
        print("Jasiek przeszedl cala droge: ", v*100)
        i=input("Czy chsesz dalej wpisywac czas?: ")
    else:
        print("Jasiek przeszedl: ", v*t)
        i = input("Czy chsesz dalej wpisywac czas?: ")