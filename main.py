from time import sleep
from classes.Labrynth import Labrynth
from mazes.maze_1 import lab

if __name__ == '__main__':
    l = Labrynth(lab.get('lab'), lab.get('min_moves'))
    l.run()