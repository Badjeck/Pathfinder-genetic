from sys import stdout
from time import sleep
from random import random, randrange
from typing import Tuple
from classes.Parameters import Parameters
from classes.colors import renderEnd, renderPath, renderStart, renderWall
from classes.mr_larbin import mr_larbin

class Labrynth:
    def __init__(self, newLabrynth:list[list], min_moves:int, moves_list:list[str]=None, agent:mr_larbin=None):
        self.labrynth   = newLabrynth
        self.rows       = len(newLabrynth)
        self.columns    = len(newLabrynth[0])
        self.min_moves  = min_moves if min_moves else 5
        self.start      = self.searchInLab(case='e')
        self.end        = self.searchInLab(case='s')
        self.isValid    = False

        if moves_list :
            self.moves_list = moves_list.copy()
            self.mutate()
        else :
            self.moves_list = self.generateMoveList()

        if agent:
            self.agent  = agent
        else:
            self.agent = mr_larbin(newPosition=self.start)

        if self.labrynth and self.start and self.end and self.agent:
            self.isValid = True

    def __str__(self) -> str:
        return str(self.agent)

    def searchInLab(self, case:str=None, place:Tuple=None):
        if case:
            i = 0
            while i < self.rows:
                j = 0
                while j < self.columns:
                    if self.labrynth[i][j] == case:
                        return {
                            'field': case,
                            'position': (i, j)
                        }
                    j += 1
                i += 1
            return {
                'field': None,
                'position': (-1, -1)
            }
        elif place:
            try:
                if place[0] > self.rows or place[0] < 0:
                    return {
                        'field': None,
                        'position': (-1, -1)
                    }
                elif place[1] > self.columns or place[1] < 0:
                    return {
                        'field': None,
                        'position': (-1, -1)
                    }
                else:
                    return {
                        'field': self.labrynth[place[0]][place[1]],
                        'position': (place[0], place[1])
                    }
            except IndexError:
                return {
                    'field': None,
                    'position': (-1, -1)
                }
        else:
            return {
                'field': None,
                'position': (-1, -1)
            }

    def getStart(self):
        if self.start:
            return self.start
        else:
            self.start = self.searchInLab('e')
            return self.start

    def getEnd(self):
        if self.end:
            return self.end
        else:
            self.end = self.searchInLab('e')
            return self.end

    def generateMoveList(self):
        return [ Parameters.randomDirection() for _ in range(self.min_moves) ]

    def moveAgent(self, direction: str, showMaze: bool=True):
        if direction in Parameters.directions.keys():
            match direction:
                case 'left':
                    newPos = self.searchInLab(place=(self.agent.getPosition().get('position')[0], self.agent.getPosition().get('position')[1]-1))
                case 'up':
                    newPos = self.searchInLab(place=(self.agent.getPosition().get('position')[0]-1, self.agent.getPosition().get('position')[1]))
                case 'right':
                    newPos = self.searchInLab(place=(self.agent.getPosition().get('position')[0], self.agent.getPosition().get('position')[1]+1))
                case 'down':
                    newPos = self.searchInLab(place=(self.agent.getPosition().get('position')[0]+1, self.agent.getPosition().get('position')[1]))

            if newPos.get('field') == 'p' or newPos.get('field') == 'e':
                self.agent.moveTo(newPos=newPos, direction=direction)
            elif newPos.get('field') == 'w':
                self.agent.moveTo(direction=direction)
            elif newPos.get('field') == 's':
                self.agent.moveTo(newPos=newPos, direction=direction)

            self.agent.updateFitness(self.end.get('position'))
            if showMaze:
                self.showMaze(agent=True)

    def showMaze(self, agent:bool = None):
        i = 0
        columns = []
        while i < self.rows:
            j = 0
            row = []
            while j < self.columns:
                isAgent = agent and self.agent.getPosition().get('position')[0] == i and self.agent.getPosition().get('position')[1] == j

                match self.labrynth[i][j]:
                    case 'w':
                        row.append(renderWall(isAgent))
                    case 'p':
                        row.append(renderPath(isAgent))
                    case 'e':
                        row.append(renderStart(isAgent))
                    case 's':
                        row.append(renderEnd(isAgent))
                j += 1
            columns.append(row)
            i += 1

        print('\n'.join([''.join(a) for a in columns]), end='\x1b[1K\r')

    def showCell(self, position):
        i = 0
        columns = []
        while i < self.rows:
            j = 0
            row = []
            while j < self.columns:
                isAgent = position and position.get('position')[0] == i and position.get('position')[1] == j

                match self.labrynth[i][j]:
                    case 'w':
                        row.append(renderWall(isAgent))
                    case 'p':
                        row.append(renderPath(isAgent))
                    case 'e':
                        row.append(renderStart(isAgent))
                    case 's':
                        row.append(renderEnd(isAgent))
                j += 1
            columns.append(row)
            i += 1

        return '\n'.join([''.join(a) for a in columns])+'\n'

    def getFitness(self) :
        return self.agent.getFitness()

    def mutate(self) :
        #Si on peu muter
        if random() <= Parameters.mutationRatio :
            event = random()
            #On supprime un movement
            if event <= Parameters.mutationDeleteRatio :
                self.moves_list.pop(randrange(len(self.moves_list)))
            #Ou on ajoute un mouvement
            elif event > Parameters.mutationDeleteRatio or event <= Parameters.mutationAddRation :
                self.moves_list.append(Parameters.randomDirection())
            #Ou on change un mouvement
            else :
                self.moves_list[randrange(len(self.moves_list))] = Parameters.randomDirection()

    def showPace(self):
        for idx, place in enumerate(self.agent.getPlaces()):
            stdout.write('\r  ===== Coup : {} =====  \n'.format(idx))
            stdout.flush()
            stdout.write('\r{}\n'.format(self.showCell(place)))
            stdout.flush()
            sleep(1)

    def run(self, directionsList:list[str]=None):
        if directionsList:
            for direction in directionsList:
                self.moveAgent(direction=direction, showMaze=False)
        else:
            for direction in self.moves_list:
                self.moveAgent(direction=direction, showMaze=False)

