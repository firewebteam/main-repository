class Student:
    oceny = []
    nazwa = ''
    pluton = 0

    def __init__(self):
        self.oceny = []

    def in_ocena(self, oc):
        self.oceny.append(oc)

    def in_pluton(self, pl):
        self.pluton = pl

    def in_nazwa(self, nz):
        self.nazwa = nz

    def out_srednia(self):
        suma = 0
        for i in self.oceny:
            suma += i
        srednia = suma/len(self.oceny)


class Studenci():
    id_list = []
    srednie_list = []

    def __init__(self):
        self.id_list = []
        self.srednie_list = []

    def srednie(self):

        self.srednie_list.append()
