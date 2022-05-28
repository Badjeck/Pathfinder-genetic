from random import randrange
from classes.Labrynth import Labrynth
from classes.Parameters import Parameters


class Population:
    def __init__(self,lab) -> None:
        self.population=[]
        for _ in range(Parameters.populationNbr) :
            self.population.append(Labrynth(lab.get('lab'),lab.get('min_moves')))

    def __str__(self) -> str:
        return '\n'.join([str(ind) for ind in self.population])

    def evaluate_order(self) -> None:
        pass

    def selection(self):
        total_ranks = len(self.population)*(len(self.population)+1)/2
        rand = randrange(total_ranks)
        ind_index = 0
        nb_parts = len(self.population)
        total_parts = 0

        while total_parts < rand:
            ind_index+=1
            total_parts += nb_parts
            nb_parts-=1

        return self.population[ind_index]

    def run(self) -> None:
        pass