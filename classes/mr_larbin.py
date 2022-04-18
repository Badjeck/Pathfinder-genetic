from cmath import sqrt
from turtle import position


class mr_larbin:
    def __init__(self, newPosition:dict[str, tuple[int, int]], name:str="Mr Larbin", moves:list[str]=[]) -> None:
        self.name=name
        self.initialPosition = newPosition
        self.position = newPosition
        self.moves=moves
        self.fitness = -1

    def __str__(self) -> str:
        return "{} is on position ({}, {}) Far to arrival as {}".format(self.getName(), self.position.get('position')[0], self.position.get('position')[1], self.getFitness())

    def getName(self) -> str:
        return self.name

    def setName(self, new_name: str) -> None:
        self.name = new_name

    def getName(self) -> str:
        return self.name

    def setMoves(self, newMoves: list[str]) -> None:
        self.moves = newMoves

    def getMoves(self) -> list:
        return self.moves

    def addMove(self, newMove: str) -> None:
        self.moves.append(newMove)

    def removeMove(self, moveIndex: int) -> None:
        del self.moves[moveIndex]

    def setPosition(self, newPosition: dict[str, tuple[int, int]]):
        self.position = newPosition

    def getPosition(self) -> dict[str, tuple[int, int]]:
        return self.position

    def moveTo(self, direction: str, newPos: dict[str, tuple[int, int]]=None):
        self.addMove(direction)
        self.setPosition(newPos if newPos else self.getPosition())

    def setFitness(self, newFitness):
        self.fitness = newFitness

    def updateFitness(self, arrival: tuple[int, int]):
        currentPos = self.getPosition().get('position')
        self.setFitness(sqrt((arrival[0]-currentPos[0])**2+(arrival[1]-currentPos[1])**2).real)
        return self.fitness

    def getFitness(self):
        return self.fitness