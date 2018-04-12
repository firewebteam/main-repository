v = 3.8

a = "tak"
while a == "tak":
    t = float(input("Podaj czas: "))
    if t>100:
        print("Jasiek ukończył trasę", v*100)
        a = input("Podać inny czas?")
    else:
        print("Jasiek przeszedł", v*t)
        a = input("Podać inny czas?")