from common import *
sum = 0
for line in readfile():
    a,b,c = map(int, line.strip().split("x"))
    min1 = min(a,b,c)
    remaining = [a,b,c]
    remaining.remove(min1)
    min2 = min(remaining)
    sum += 2*(min1+min2) + a*b*c
print sum
