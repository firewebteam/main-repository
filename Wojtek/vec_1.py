import numpy as np
import matplotlib.pyplot as plt

## program obrazujący w postaci animacji tor ruchu auta w kolejnych sekundach ruchu na podstawie położenia pocz
## położenia końcowego i prędkości

class Drive_by:
    def __init__(self, v, ptA, ptB):
        self.velocity = v
        self.start = np.array(ptA)
        self.end = np.array(ptB)
        self.step = 1
        self.trajectory = []

    def create_trajectory(self):
        vec_real = np.array(self.end - self.start)      # wspolrzedne wektora rzeczywistego
        len_vec_real = np.linalg.norm(vec_real)         # dlugosc wektora rzeczywistego
        vec_u = [vec_real[0]/len_vec_real, vec_real[1]/len_vec_real]        # wspolrzedne wektora jednostkowego(majacego dlugosc 1)
        for i in range(3, 10, 1):         # tworze trajektorie od 1s do  10 s, co 1s
            x = vec_u[0] * self.velocity * i
            y = vec_u[1] * self.velocity * i
            self.trajectory.append((x, y))
        print(self.trajectory)

    def create_chart(self):
        self.create_trajectory()
        fig = plt.figure()
        x, y = zip(*self.trajectory)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(x, y, 'ro', linestyle="-")
        plt.show()

    def create_animation(self):
        pass


a = Drive_by(5, (2, 3), (9, 18))
a.create_chart()
