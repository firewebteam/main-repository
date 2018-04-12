from numpy import random as rd
import json

file = open("D:\eggman.json", 'r')
dic = json.load(file)
first_floor = dic["1"]["EVACUEES"]
v_distance = 12

class Evacuee:
    def __init__(self, h_s, v_s, p_e):
        self.h_speed = h_s
        self.v_speed = v_s
        self.pre_evacuation = p_e
        self.h_distance = rd.uniform(10, 80, 1)
        self.time = self.pre_evacuation + v_distance/self.v_speed + self.h_distance/self.h_speed



class Evacuees:
    def __init__(self, lista):
        self.evacuees = lista

    def add_peds(self, p):
        self.evacuees = p

    def get_evacuation_time(self):
        self.time = []

        for i in self.evacuees:
            self.time.append(i.time)

        return max(self.time)

    def get_lagger(self, a):
        ev_id = self.time.index(a)
        return ev_id


evacs = []
i = 0

for k, v in first_floor.items():
    h_s = first_floor[k]["H_SPEED"]
    v_s = first_floor[k]["V_SPEED"]
    p_e = first_floor[k]["PRE_EVACUATION"]
    evacs.append(Evacuee(h_s, v_s, p_e))
    i += 1

ev_total = Evacuees(evacs)
lag = ev_total.get_evacuation_time()
lag = float(lag)
name = ev_total.get_lagger(lag)
print("The last evacuee was E{} with {}s time.".format(name, lag))
