from turtle import right


class Parameters:
    directions = {
        'left':     (-1,  0),
        'up':       ( 0, -1),
        'right':    ( 1,  0),
        'down':     ( 0,  1)
    }
    nbMoves=50
    nbIterations=10
    mutationRatio=0.5