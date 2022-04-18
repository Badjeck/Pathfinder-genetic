'''
Text color	Code	Text style	Code	Background color	Code
Black	    30	    No effect	0	    Black	            40
Red	        31	    Bold	    1	    Red                 41
Green	    32	    Underline	2	    Green	            42
Yellow	    33	    Negative1	3	    Yellow	            43
Blue	    34	    Negative2	5	    Blue	            44
Purple	    35			                Purple	            45
Cyan	    36			                Cyan	            46
White	    37			                White	            47

Escape code     Font style  Text color  Background color
\033[           1;          32;         40m
'''

class colors:
    reset   = '\033[0m' #RESET COLOR
    wall    = '\033[3;30;40m'
    wallA   = '\033[3;37;40m'
    path    = '\033[3;31;41m'
    pathA   = '\033[3;30;41m'
    start   = '\033[3;32;42m'
    startA  = '\033[3;30;42m'
    end     = '\033[3;33;43m'
    endA    = '\033[3;30;43m'

def renderWall(agentOnPos:bool=None):
    if agentOnPos:
        return colors.wall+"\u2588"+colors.wallA+"X"+colors.wall+"\u2588"+colors.reset
    else:
        return colors.wall+"\u2588\u2588\u2588"+colors.reset

def renderPath(agentOnPos:bool=None):
    if agentOnPos:
        return colors.path+"\u2588"+colors.pathA+"X"+colors.path+"\u2588"+colors.reset
    else:
        return colors.path+"\u2588\u2588\u2588"+colors.reset

def renderStart(agentOnPos:bool=None):
    if agentOnPos:
        return colors.start+"\u2588"+colors.startA+"X"+colors.start+"\u2588"+colors.reset
    else:
        return colors.start+"\u2588\u2588\u2588"+colors.reset

def renderEnd(agentOnPos:bool=None):
    if agentOnPos:
        return colors.end+"\u2588"+colors.endA+"X"+colors.end+"\u2588"+colors.reset
    else:
        return colors.end+"\u2588\u2588\u2588"+colors.reset