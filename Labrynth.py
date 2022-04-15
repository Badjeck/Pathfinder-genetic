from typing import Tuple
from Static import colors


class Labrynth:
    def __init__(self, newLabrynth=list[list]):
        self.labrynth   = newLabrynth
        self.rows       = len(newLabrynth)
        self.columns    = len(newLabrynth[0])
        self.start      = self.searchInLab(case='e')
        self.end        = self.searchInLab(case='s')

    def searchInLab(self, case:str=None, place:Tuple=None):
        if case:
            i = 0
            while i < self.rows:
                j = 0
                while j < self.columns:
                    if self.labrynth[i][j] == case:
                        return (i, j)
                    j += 1
                i += 1
            return (-1, -1)
        elif place:
            if place[0] > self.rows or place[0] < 0:
                print('given x out of range')
            elif place[1] > self.columns or place[1] < 0:
                print('given y out of range')
            else:
                return self.labrynth[place[0]][place[1]]

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

    def show(self):
        i = 0
        columns = []
        while i < self.rows:
            j = 0
            row = []
            while j < self.columns:
                match self.labrynth[i][j]:
                    case 'w':
                        row.append(colors.wall+u"\u2588\u2588"+colors.reset)
                    case 'p':
                        row.append(colors.path+u"\u2588\u2588"+colors.reset)
                    case 'e':
                        row.append(colors.start+u"\u2588\u2588"+colors.reset)
                    case 's':
                        row.append(colors.end+u"\u2588\u2588"+colors.reset)
                j += 1
            i += 1
            columns.append(''.join(row))

        print('\n'.join(columns))