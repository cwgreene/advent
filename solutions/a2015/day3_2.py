from common import *

MOVE = {"<" : (-1,0),
        ">" : (1,0),
        "^" : (0,1),
        "v" : (0,-1)}

positions = set()

def move(santa, direction):
    x, y = santa
    return x + MOVE[direction][0], y + MOVE[direction][1]

for line in readfile():
    santa = 0,0
    robosanta = 0,0
    keys = ["santa", "robosanta"]
    santa_locations = {"santa" : santa, "robosanta" : robosanta}
    curkey = 0
    for direction in line.strip():
        x, y = santa_locations[keys[curkey]]
        santa_locations[keys[curkey]] = move((x, y), direction)
        positions.add((x,y))
        curkey = (curkey + 1) % 2
    print len(positions)
