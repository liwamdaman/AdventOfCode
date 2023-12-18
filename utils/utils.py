import time

def timeFunction(function, *args):
    begin = time.time()
    function(*args)
    end = time.time()
    print("Time elapsed = " + str(end-begin))

def parseLinesToMatrix(lines):
    matrix =[]
    for line in lines:
        matrix.append([])
        for c in line:
            matrix[-1].append(c)
    return matrix

def prettyPrintMatrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end="")
        print()
    print()

def prettyPrintLines(lines):
    for line in lines:
        print(line)
    print()

def getRotated90CWLines(lines):
    # Found this on https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    return list(zip(*lines[::-1]))

def getRotated90CWMatrix(matrix):
    return [list(x) for x in zip(*matrix[::-1])]