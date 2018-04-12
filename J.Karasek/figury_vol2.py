class Figury:

    def __init__(self, figure, x, y, color):
        self.figure = figure
        self.x = x
        self.y = y
        self.color = color
        print("Powstała figura:", self.figure)

    def figure_color(self):
        print("Ta figura ma kolor", self.color)

    def figure_area(self):
        if self.figure == "prostokąt":
          area = float(self.x * self.y)
          print("Pole figury wynosi", area)
        elif self.figure == "trójkąt":
          area = float(0.5*self.x * self.y)
          print("Pole figury wynosi", area)
        elif self.figure == "trapez":  #h = 10
          area = float(((self.x + self.y)/2)*10)
          print("Pole figury wynosi", area)
        elif self.figure == "romb": #y to wysokość
            area = float(self.x * self.y)
            print("Pole figury wynosi", area)
        else:
            print("Nie mogę policzyć pola")


figura1 = Figury("prostokąt", 3, 5 ,"zielony")
figura1.figure_color()
figura1.figure_area()

figura2 = Figury("trójkąt", 4, 6, "pomarańczowy")
figura2.figure_color()
figura2.figure_area()

figura3 = Figury("trapez", 10, 6, "różowy")
figura3.figure_color()
figura3.figure_area()

figura4 = Figury("romb", 4, 2, "niebieski")
figura4.figure_color()
figura4.figure_area()
