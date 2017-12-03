import re
from common import *

nice = 0
def isnice(string):
    if not re.match(r".*[aeiou].*[aeiou].*[aeiou].*", string):
        return False
    if not re.match(r".*(.)\1.*", string):
        return False
    if re.match(r".*(ab|cd|pq|xy).*", string):
        return False
    return True

for line in readfile():
    if isnice(line.strip()):
        nice += 1
print nice
