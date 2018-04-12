class Figury():


    def __init__(self, kolor, x, y):
        self.kolor = kolor
        self.x = x
        self.y = y

    def prostokat(self):
        print("Pole prostokata to", self.x*self.y)
        print("Kolor prostokąta to", self.kolor)
    def trojkat(self):
        print("Pole trójkąta to", (self.x*self.y)/2)
        print("Kolor trójkąta to", self.kolor)

    def trapez(self):
        print("Pole trapezu to", ((self.x*self.y)/2)*10)
        print("Kolor trapezu to", self.kolor)

    def romb(self):
        print("Pole rombu to", self.x*self.y)               #y w tym przypadku to wysokość
        print("Kolor rombu to", self.kolor)


prostokat=Figury("żółty", 5, 11)
prostokat.prostokat()
trojkat=Figury("niebieski", 12, 8)
trojkat.trojkat()
trapez=Figury("zielony", 6, 16)
trapez.trapez()
romb=Figury("brązowy", 4, 6)
romb.romb()




