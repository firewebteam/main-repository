import numpy.random as random


class Pedestrian:
    def __init__(self):
        self.s = random.normal(1.2, 0.2, 1)
        self.d = random.uniform(10, 80, 1)
        self.t = self.d / self.s
        self.t = float(self.t)


class Evacuates:
    def __init__(self):
        self.pedestrians = []

    def add_peds(self, p):
        self.pedestrians = p

    def get_evacuation_time(self):
        self.time = []

        for i in self.pedestrians:
            self.time.append(i.t)

        return max(self.time)

    def get_lagger(self, a):
        ped_id = self.time.index(a)
        return ped_id


peds = []

for i in range(100):
    peds.append(Pedestrian())

ev = Evacuates()
ev.add_peds(peds)
x = ev.get_evacuation_time()
y = ev.get_lagger(x)
print('The last evacuate is {} with {}s evacuation time.'.format(y, x))

