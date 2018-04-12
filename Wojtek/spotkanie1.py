from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.patches import Ellipse

# animacje za pomocą funkcji
# ZADANIE: animować wykres ewakuacji, wykombinować coś z animacją poniżej


class Anim:

    def __init__(self):
        self.fig = plt.figure()     # tworzy nowe okno
        self.record = False         # parametr nagrywania
        self.pedestrians = []       #
        self.n_frames = 0           # ilość klatek
        self.trajectory = []        # zbiór punktów (trasa)
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

        x = np.arange(0, 10, 0.1)   # tworzenie tabeli "xów" (min, max, moduł)
        for i in x:
            coord = [(i, 1), (i+1, 2)]
            self.trajectory.append(coord)   # tworzenie trasy ze współrzędnych (par pktów)
        self.n_frames = len(self.trajectory)    # ilość klatek odpowiada ilości punktów na trasie
        elipses = [Ellipse(i, width=1, height=0.5, angle=0) for i in self.trajectory[0]]  # stworzenie kształtu i przypisanie mu cech (wymiary, współ początkowych)
        [self.pedestrians.append(self.ax.add_patch(elipses[i])) for i in range(len(elipses))]   # przypisuje kształty (z jego parametrami) do osi w formie tabeli

    def init_animation(self):
        [self.pedestrians[i].set_visible(True) for i in range(len(self.pedestrians))]      # zezwala na wyświetlanie kształtów
        return self.pedestrians

    def animate(self, i):       # funkcja wywołująca następne klatki przy kolejnych powtórzeniach pętli
        for j in range(len(self.pedestrians)):
            self.pedestrians[j].center = self.trajectory[i][j]  # pokrywa środek elipsy ze środkiem wg współrzędncyh
        return self.pedestrians

    def do_animation(self, n_interval):     # właściwa funkcja tworząca animację
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_animation, frames=self.n_frames,
                                       interval=n_interval, blit=True)
        print(self.trajectory)
        if self.record:
            pass        # tu znalazłoby się odniesienie do nagrywnia, lecz kodeków brak
        plt.show()


a = Anim()
a.do_animation(50)
