import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import patches as mpaths
import json
import rvo2

#ZAD_DOM:
#  - kilku z uciekinierów ma pik przed pierwszym krokiem (w lewym górnym rogu) - do naprawy
#  - pobrać wszystkie możliwe dane z eggman.json, a nie deklarować w programie na stałe


class Pedestrian:
    def __init__(self, map, speed, pre):
        self.position = map[0]
        self.velocity = self.create_vel_vector(map[0], map[1])
        self.speed = speed
        self.road_map = map
        self.goal_no = 1
        self.pre_time = pre

    def create_vel_vector(self, actual, goal):
        vec_real = np.array(goal) - np.array(actual)  # wspolrzedne wektorow rzeczywistych aby z warunku brało goals_no
        len_vec_real = np.linalg.norm(vec_real)
        vec_u = vec_real / len_vec_real
        [float(i) for i in vec_u]
        return tuple(vec_u)

    def chart(self):
        self.do_it()
        x, y = zip(*self.traj)
        plt.plot(x, y, "-o")
        plt.show()


class Pedestrians:
    def __init__(self):
        self.peds = []
        self.sim_time = 100
        self.step_time = 0.1

    def add_pedestrians(self, ped):
        self.peds.append(ped)
# NIECH PRZEŁĄCZA CEL ODPOWIEDNIO!!!!!
    def check_goal(self, agent_no):
        actual = np.array(self.peds[agent_no].position)
        next = np.array(self.peds[agent_no].road_map)
        try:
            dist = np.linalg.norm(actual - next[self.peds[agent_no].goal_no])
            if dist < 0.9 and self.peds[agent_no].goal_no <= range(self.peds[agent_no].road_map):
                self.peds[agent_no].goal_no += 1
        except:
            pass

    def great_loop(self):
        traj = []
        # kolejne kroki:
        for j in range(int(self.sim_time/self.step_time)):
            step_traj = []
            # kolejni agenci w jednym z kroków:
            for i in range(sim.getNumAgents()):
                self.check_goal(i)
                self.peds[i].velocity = self.peds[i].create_vel_vector(self.peds[i].position, self.peds[i].road_map[self.peds[i].goal_no])
                sim.setAgentPrefVelocity(sim_agents[i], self.peds[i].velocity)
                print(self.peds[i].velocity)
                step_traj.append(sim.getAgentPosition(sim_agents[i]))
                self.peds[i].position = sim.getAgentPosition(sim_agents[i])
            traj.append(step_traj)
            sim.doStep()
        return traj

    #DELETE uzyj zamiast tego greatloop
    def get_trajectories(self):
        trajectories = []
        for i in self.peds:
            trajectories.append(i.do_it())
        return trajectories

    #DELETE uzyj greatloop
    def get_chart(self):    #tworzy trajektorię kroków, która służy do tworzenia animacji
        trajs = self.get_trajectories()
        temp_traj = []
        lens = []

        for i in trajs:
            lens.append(len(i))
        length = max(lens)
        for i in range(length):          # dla iluśtam kroków
            step = []
            for j in range(len(trajs)):  # tworzy gdzie są w danym kroku
                try:
                    step.append(trajs[j][i])
                except:
                    step.append(trajs[j][-1])
            temp_traj.append(step)          #do tego momentu tworzy odpowiednią trajektorię
        #print('trajektoria posortowana wg krokow:', temp_traj)

        foo = zip(*temp_traj)               #rysuje trajektorie
        for i in foo:
            x, y = zip(*i)
            plt.plot(x, y, "-")

        return temp_traj


class Animation:
    def __init__(self, pedest):
        self.pedest = pedest
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-1, 60), ylim=(-1, 20))
        self.trial = []
        self.ang = 0
        self.create_walls()
        self.trajectory = pedest.great_loop()
        #print(self.trajectory)
        self.n_frames = len(self.trajectory)

        elipses = [mpaths.Ellipse(i, width=.3, height=.3, angle=self.ang) for i in
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

    def create_walls(self):
        obst = files_opening()[1]
        for i in obst:                                      # kreślenie ścian budynku
            corners_x = [i[0][0], i[1][0], i[2][0], i[3][0]]
            corners_y = [i[0][1], i[1][1], i[2][1], i[3][1]]
            plt.plot(corners_x, corners_y, "r", lw=3)


def convert_data(eggman_ped):
    #print(eggman_ped)
    speed = eggman_ped["H_SPEED"]
    goals = [eggman_ped['ORIGIN']]
    goals.extend(eggman_ped['ROADMAP'])
    pre = eggman_ped["PRE_EVACUATION"]

    return goals, speed, pre


def files_opening():
    file1 = open("//home/wojtas/PythonFiles/main-repository/Python - zadania/ewakuacja2/eggman.json", 'r')
    first_floor = json.load(file1)["1"]["EVACUEES"]
    file2 = open("//home/wojtas/PythonFiles/main-repository/Python - zadania/ewakuacja2/geom.json", "r")
    obst = json.load(file2)["obstacles"]["1"]
    for k, v in first_floor.items():
        temp_ped = Pedestrian(*convert_data(v))
        a.add_pedestrians(temp_ped)
    return first_floor, obst


file2 = open("//home/wojtas/PythonFiles/main-repository/Python - zadania/ewakuacja2/geom.json", "r")
obst = json.load(file2)["obstacles"]["1"]

a = Pedestrians()
files_opening()

sim = rvo2.PyRVOSimulator(0.1, 0.8, 5, 1, 0.05, .3, 2)
sim_agents = []
for i in a.peds:
    sim_agents.append(sim.addAgent(tuple(i.road_map[0])))
    sim.setAgentPrefVelocity(sim_agents[len(sim_agents)-1], i.create_vel_vector(i.road_map[0], i.road_map[1]))
for i in obst:
    sim.addObstacle(i)
sim.processObstacles()


x = Animation(a)   #(klasa zbiorcza agentów, czas trwania animacji
x.do_animation(100)     #(odstęp miedzy klatkami [ms])
