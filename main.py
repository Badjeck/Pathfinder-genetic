from time import sleep
from classes.Labrynth import Labrynth
from classes.Population import Population
from mazes.maze_2 import lab

if __name__ == '__main__':
    pop = Population(lab)
    pop.run()