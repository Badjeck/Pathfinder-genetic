from typing import Tuple
from classes.Parameters import Parameters


class mr_larbin:
    def __init__(self, name:str="Mr Larbin", new_x_pos:int=None, new_y_pos:int=None) -> None:
        self.__name=name
        self.__x_pos=new_x_pos if new_x_pos else None
        self.__y_pos=new_y_pos if new_y_pos else None
        self.__moves=[]

    def getName(self) -> str:
        return self.__name

    def setName(self, new_name: str) -> None:
        self.__name = new_name

    def getName(self) -> str:
        return self.__name

    def setXPos(self, newXPos: int) -> None:
        self.x_pos = newXPos

    def getXPos(self) -> int:
        return self.__x_pos

    def setYPos(self, newYPos: int) -> None:
        self.__y_pos = newYPos

    def getYPos(self) -> int:
        return self.__y_pos

    def updatePos(self, new_pos:Tuple) -> None:
        self.setXPos(new_pos[0])
        self.setYPos(new_pos[1])

    def addMove(self, move: str) -> None:
        if move in Parameters.directions.keys():
            self.__moves.append(move)
        else:
            print('Wrong move given : {}'.format(move))

    def move(self, new_direction):
        if new_direction in Parameters.directions.keys():
            self.updatePos(Parameters.directions.get(new_direction))
            self.addMove(new_direction)
        else:
            print('Wrong move given : {}'.format(new_direction
            ))