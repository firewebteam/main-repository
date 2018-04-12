class Figury():

    def __init__(self, kolor, x, y):
        self.kolor=kolor
        self.x=x
        self.y=y

    def prostakat(self):
        print("Pole prostakata = ", self.x*self.y)
        print("Kolor prostokata to ", self.kolor)

    def trojkat(self):
        print("Pole trojkata = ", self.x*self.y/2)
        print("Kolor trojkata to ", self.kolor)

    def trapez(self):
        print("Pole trapezu = ", (self.x+self.y)*10/2)
        print("Kolor trapezu to ", self.kolor)



prostakat=Figury("czerwony", 10, 5)
trojkat=Figury("zolty", 6, 7)
trapez=Figury("niebieski", 4,2)

prostakat.prostakat()
trojkat.trojkat()
trapez.trapez()