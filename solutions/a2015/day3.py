from common import *

MOVE = {"<" : (-1,0),
        ">" : (1,0),
        "^" : (0,1),
        "v" : (0,-1)}

positions = set()

for line in readfile():
    x,y = 0,0
    for direction in line.strip():
        x,y = x + MOVE[direction][0], y + MOVE[direction][1]
        positions.add((x,y))
    print len(positions)
