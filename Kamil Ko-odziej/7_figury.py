class Figury:
    kolor = ""
    x = 0
    y = 0

    def prostokat(self):
        print("Kolor prostokata:", self.kolor)
        print("Pole prostakata wynosi:", self.x * self.y)

    def trojkat(self):
        print("Kolor trojkata:", self.kolor)
        print("Pole trojkata wynosi:", self.x * self.y / 2)

    def trapez(self):
        print("Kolor trapezu:", self.kolor)
        print("Pole trapezu wynosi:", (self.x + self.y) * 10 / 2)

    def romb(self):
        print("Kolor rombu:", self.kolor)
        #print("Pole rombu wynosi:" )


pr = Figury()
pr.kolor = "zielony"
pr.x = 2
pr.y = 5

trojkat = Figury()
trojkat.kolor = "różowy"
trojkat.x = 12
trojkat.y = 10

trapez = Figury()
trapez.kolor = "czerwony"
trapez.x = 1
trapez.y = 22

romb = Figury()
romb.kolor = "niebieski"
romb.x = 12
romb.y = 15

pr.prostokat()
trojkat.trojkat()
trapez.trapez()
romb.romb()