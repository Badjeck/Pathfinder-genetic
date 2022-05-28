from time import sleep
from classes.Labrynth import Labrynth
from classes.Population import Population
from mazes.maze_1 import lab

if __name__ == '__main__':
    pop = Population(lab)
    pop.run()

    # l = Labrynth(lab.get('lab'), lab.get('min_moves'))
    # l.run()