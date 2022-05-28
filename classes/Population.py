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
        for labrynth in self.population :
            labrynth.run()

        self.population.sort(key=lambda x: x.getFitness(), reverse=False)

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
        isWin = False
        generation = 1
        self.evaluate_order()

        for g in range(Parameters.nbIterations) :
            print('  ===== GENERATION {} =====  '.format(g))

            newPopulation = []
            #roue biaiseé
            newPopulation.append(self.population[0])
            #nouvelle generation
            while len(newPopulation) <= Parameters.populationNbr :
                parent = self.selection()
                newPopulation.append(Labrynth(parent.labrynth,parent.min_moves,parent.moves_list))
            self.population = newPopulation

            self.evaluate_order()
            if self.population[0].getFitness() == 0 :
                isWin = True
                break
            else :
                generation += generation
                print("=====================================")

        if isWin :
            print("Mr larbin à trouvé la sortie à la génération", generation)
        else :
            print("Mr larbin n'as pas trouvé la sortie")
            print(self.population[0].__str__())
