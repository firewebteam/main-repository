import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
from math import sqrt

# program obrazujący w postaci animacji tor ruchu obiektow w kolejnych sekundach ruchu na podstawie położenia poczatkowego,
# położenia końcowego i prędkości

# TO_DO
#       - warunek nie pozwalający przekroczyć punktu końcowego


class Drive_by:
    def __init__(self, v, ptsa, ptsb):
        self.velocity = v
        self.start = np.array(ptsa)
        self.end = np.array(ptsb)
        self.step = 1
        self.trajectory = []

    def create_trajectory(self):
        vec_real = np.array(self.end - self.start)      # wspolrzedne wektorow rzeczywistego
        len_vec_real = []
        [len_vec_real.append(sqrt(vec_real[i][0] ** 2 + vec_real[i][1] ** 2)) for i in range(len(vec_real))]   # dlugosc wektorow rzeczywistego
        vec_u = []
        [vec_u.append(vec_real[i]/len_vec_real[i]) for i in range(len(vec_real))]    # wspolrzedne wektorow jednostkoweych(majacego dlugosc 1)

        for i in range(1, 10, self.step):         # tworze trajektorie od 1s do  10 s, co 1s
            temp = []
            for j in vec_u:
                x = j[0] * self.velocity * i
                y = j[1] * self.velocity * i

                temp.append((x, y))
            self.trajectory.append(temp)
        print('trajectory=', self.trajectory)

    def create_chart(self):
        self.create_trajectory()

        x = []
        y = []
        for i in self.trajectory:
            mid_traj_x = []
            mid_traj_y = []
            for j in i:
                mid_traj_x.append(j[0])
                mid_traj_y.append(j[1])
            x.append(mid_traj_x)
            y.append(mid_traj_y)
        print('x =', x)
        print('y =', y)

        plt.xlabel("x")
        plt.ylabel("y")

        return x, y


class Animation:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
        self.n_frames = 0
        self.trial = []
        self.ang = 0

        a = Drive_by(10, start_list, end_list)
        x, y = a.create_chart()

        plt.plot(x, y, linewidth=2)

        self.trajectory = a.trajectory
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=5, height=5, angle=self.ang) for i in
                   self.trajectory[0]]      # stworzenie kształtu i przypisanie mu cech (wymiary, współ początkowych)
        [self.trial.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]

    def init_animation(self):
        [self.trial[i].set_visible(True) for i in range(len(self.trial))]

        return self.trial

    def animate(self, i):
        for j in range(len(self.trajectory[0])):
            self.trial[j].center = self.trajectory[i][j]
        return self.trial

    def do_animation(self, n_interval):
        print('n_frames=', self.n_frames)
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation,
                                     interval=n_interval, blit=True)
        plt.show()


start_list = [(2, 3), (100, 100), (2, 3)]
end_list = [(9, 18), (10, 10), (8, 20)]

c = Animation()
c.do_animation(1000)
