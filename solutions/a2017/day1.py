from common import *

sum = 0
for line in readfile():
    cur = None
    for char in line + line[0]:
        if char == cur:
            sum += int(char)
            cur = char
        else:
            cur = char
print sum
