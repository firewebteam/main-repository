import rvo2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths


sim = rvo2.PyRVOSimulator(0.1, 1.5, 5, 1.5, 2, .4, 2)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
a0_start = (0, 0)
a0_goal = (10, 0)
a1_start = (10, 0)
a1_goal = (-10, 0)
a0 = sim.addAgent(a0_start)
a1 = sim.addAgent(a1_start)
#a2 = sim.addAgent((1, 1))
#a3 = sim.addAgent((0, 1), 1.5, 5, 1.5, 2, 0.4, 2, (0, 0))

# Obstacles are also supported.
#o1 = sim.addObstacle([(0.5, 0.025), (0.5, -0.025), (0.65, 0.025), (0.65, -0.025)])
#sim.processObstacles()

sim.setAgentPrefVelocity(a0, a0_goal)
sim.setAgentPrefVelocity(a1, a1_goal)
#sim.setAgentPrefVelocity(a2, (-1, -1))
#sim.setAgentPrefVelocity(a3, (1, -1))

print('Simulation has %i agents and %i obstacle vertices in it.' %
      (sim.getNumAgents(), sim.getNumObstacleVertices()))


def create_vel_vector(actual, goal, velo):
    vec_real = np.array(goal) - np.array(actual)  # wspolrzedne wektorow rzeczywistych aby z warunku brało goals_no
    len_vec_real = np.linalg.norm(vec_real)
    vec_u = vec_real / len_vec_real
    x, y = vec_u*velo
    vec_vel = (x, y)
    return vec_vel

print('Running simulation')
trajectory = []

for step in range(100):
    a0_position = sim.getAgentPosition(a0)
    a1_position = sim.getAgentPosition(a1)
    sim.setAgentPrefVelocity(a0, create_vel_vector(a0_position, a0_goal, 1))                #dokończ dla tych dwóch dynamiczną zmianę wektora prędkości
    sim.setAgentPrefVelocity(a1, create_vel_vector(a1_position, a1_goal, 4))
    sim.doStep()

    positions = ['(%.3f, %.3f)' % sim.getAgentPosition(i) for i in (a0, a1)]
    x, y = (sim.getAgentPosition(i) for i in (a0, a1))
    trajectory.append([x, y])
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), str(positions)))



class Animation:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-11, 11), ylim=(-1, 1))
        self.n_frames = 0
        self.trial = []
        self.ang = 0


        self.trajectory = trajectory
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=1, height=1, angle=self.ang) for i in
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
        animate = anim.FuncAnimation(self.fig, self.animate, frames=self.n_frames, init_func=self.init_animation,
                                     interval=n_interval, blit=True)
        plt.show()
        plt.close()

x = Animation()
x.do_animation(100)
