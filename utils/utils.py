import time

def timeFunction(function, *args):
    begin = time.time()
    function(*args)
    end = time.time()
    print("Time elapsed = " + str(end-begin))

def prettyPrintMatrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end="")
        print()

def prettyPrintLines(lines):
    for line in lines:
        print(line)
    print()