import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import animation

file1 = open("C:\pliki_py\eggman.json", 'r')
first_floor = json.load(file1)["1"]["EVACUEES"]
file2 = open("C:\pliki_py\geom.json", "r")
obst = json.load(file2)["obstacles"]["1"]
v_distance = 12


class Evacuee:
    def __init__(self, hs, vd, pe, hd):
        self.h_speed = hs
        self.v_speed = vd
        self.pre_evacuation = pe
        self.h_distance = hd
        self.time = self.pre_evacuation + v_distance/self.v_speed + self.h_distance/self.h_speed


class Evacuees:
    def __init__(self):
        self.time = []
        self.evacs = []
        self.points = []


    def get_evacuation_time(self):
        for i in self.create_points(first_floor):
            self.time.append(i.time)
        return max(self.time)

    def get_lagger(self):
        ev_id = self.time.index(self.get_evacuation_time())
        return ev_id

    def create_points(self, floor_dict):            # stworzenie tablicy z punktami trasy wszystkich "evacs"
        for k, v in floor_dict.items():
            h_s = floor_dict[k]["H_SPEED"]
            v_s = floor_dict[k]["V_SPEED"]
            p_e = floor_dict[k]["PRE_EVACUATION"]
            points_temp = (floor_dict[k]['ROADMAP'])
            points_temp.insert(0, floor_dict[k]['ORIGIN'])
            x, y = zip(*points_temp)
            plt.plot(x, y, "--", linewidth=1)                   # kreślenie tras
            plt.text(points_temp[0][0], points_temp[0][1], str(k))        # podpisy punktów
            h_d = 0
            j = 0
            for i in range(len(points_temp)-1):
                diff = (np.array(points_temp[j])-np.array(points_temp[j+1]))
                h_d += np.linalg.norm(diff[0] - diff[1])
                j += 1

            self.evacs.append(Evacuee(h_s, v_s, p_e, h_d))
            self.points.append([x, y])

        return self.evacs

    def create_chart(self):
        self.create_points(first_floor)
        plt.show()


class Anim():
    def __init__(self):
        self.fig = plt.figure()  # tworzy nowy wykres
        self.record = False  # parametr nagrywania
        self.n_frames = 0  # ilość klatek
        self.trajectory = []
        self.pedestrians = []
        self.create_walls()
        self.ax = plt.axes()


        circle = [Ellipse(i, c='red', width=0.1, height=0.1, angle=0) for i in self.trajectory[0]]  # stworzenie kształtu i przypisanie mu cech (wymiary, współ początkowych)
        [self.pedestrians.append(self.ax.add_patch(circle[i])) for i in range(len(circle))]   # przypisuje kształty (z jego parametrami) do osi w formie tabeli

    def create_walls(self):
        for i in obst:                                      # kreślenie ścian budynku
            corners_x = [i[0][0], i[1][0], i[2][0], i[3][0]]
            corners_y = [i[0][1], i[1][1], i[2][1], i[3][1]]
            plt.plot(corners_x, corners_y, "r", lw=3)

    def init_animation(self):
        pass
        return self.pedestrians

    def animate(self):
        for i in range(len(self.trajectory)):
            for j in range(len(self.pedestrians)):
                self.pedestrians[j].center = self.trajectory[i][j]  # pokrywa środek elipsy ze środkiem wg współrzędncyh
                x, y = self.trajectory[i]
                plt.plot(x, y, 'bo')
            return self.pedestrians

    def do_animation(self, n_interval):

        anim = animation.FuncAnimation(self.fig,self.animate, init_func=self.init_animation, frames=self.n_frames,
                                       interval=n_interval, blit=True)
        plt.show()


a = Evacuees()
a.create_chart()
b = Anim()
b.do_animation(50)

print("The last evacuee was E{} with {}s time.".format(a.get_lagger(), a.get_evacuation_time()))
