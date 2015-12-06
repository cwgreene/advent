from common import *

import hashlib

def compute(string):
    num = 0
    while True:
        md5 = hashlib.md5(string + str(num))
        if md5.hexdigest().startswith("00000"):
            break
        num += 1
    return num 

for line in readfile():
    print compute(line.strip())
