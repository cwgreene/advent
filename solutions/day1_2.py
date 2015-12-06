from common import *

for line in readfile():
    floor = 0
    for pos, char in enumerate(line.strip(), 1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            break
    print pos

