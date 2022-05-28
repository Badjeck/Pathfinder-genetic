from random import randint

class Parameters:
    directions = {
        'left':     (-1,  0),
        'up':       ( 0, -1),
        'right':    ( 1,  0),
        'down':     ( 0,  1)
    }
    nbIterations=10
    mutationRatio=0.5
    populationNbr=10

    mutationDeleteRatio=0.1
    mutationAddRation= mutationDeleteRatio + 0.2
    mutationDirectionRatio = 1 - mutationDeleteRatio - mutationAddRation

    def randomDirection():
        rndm = randint(0, 3)

        match (rndm):
            case 0:
                return 'right'

            case 1:
                return 'left'
                
            case 2:
                return 'down'

            case 3:
                return 'up'