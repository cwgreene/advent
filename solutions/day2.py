from common import *
sum = 0
for line in readfile():
    a,b,c = map(int, line.strip().split("x"))
    sum += 2*(a*b + b*c + a*c) + min(a*b,b*c,a*c)
print sum
