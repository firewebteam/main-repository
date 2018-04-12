import numpy as np
import matplotlib.pyplot as plt


class NewMethod:
    def __init__(self, goals):
        self.traj = []
        self.start = (0, 0)
        self.speed = 1
        self.traj.append(self.start)
        self.goals = goals

    def create_vel_vector(self, actual, goal):
        vec_real = np.array(goal) - np.array(actual)  # wspolrzedne wektorow rzeczywistych aby z warunku brało goals_no
        len_vec_real = np.linalg.norm(vec_real)
        vec_u = vec_real / len_vec_real
        vec_vel = vec_u * self.speed
        return vec_vel

    def create_trajectory(self, actual, goal):
        vec_vel = self.create_vel_vector(actual, goal)

        x = actual[0] + vec_vel[0]
        y = actual[1] + vec_vel[1]
        position = (x, y)
        self.traj.append(position)
        return position, vec_vel

    def do_it(self):
        goal_no = 0
        position, vec_vel = self.create_trajectory(self.start, self.goals[goal_no])

        i = 0
        while i == 0:
            try:
                if np.linalg.norm(self.goals[goal_no] - np.array(position)) <= self.speed:
                    goal_no += 1
            except:
                break
            position, vec_vel = self.create_trajectory(position, self.goals[goal_no])

        return self.traj

    def chart(self):
        self.do_it()
        x, y = zip(*self.traj)
        plt.plot(x, y)
        plt.show()


d = NewMethod([(10, 10), (60, 30), (9, 12)])
d.chart()
