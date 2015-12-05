def set_filename(afile):
    global filename
    filename = afile

def readfile():
    afile = None
    if filename:
        afile = open(filename)
    elif len(arguments) > 1:
        afile = open(arguments[1])
    else:
        afile = sys.stdin
    return [line.strip() for line in afile.readlines()]
