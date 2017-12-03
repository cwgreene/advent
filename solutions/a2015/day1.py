from common import *

for line in readfile():
    print line.count("(") - line.count(")")
