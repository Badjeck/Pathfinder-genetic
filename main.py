from time import sleep
from classes.Labrynth import Labrynth
from mazes.maze_2 import lab

if __name__ == '__main__':
    l = Labrynth(lab)
    l.run(['right', 'right', 'down', 'right', 'down', 'down', 'right', 'down', 'right', 'down', 'right', 'down', 'right', 'down'])