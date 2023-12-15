import time

def timeFunction(function, *args):
    begin = time.time()
    function(*args)
    end = time.time()
    print("Time elapsed = " + str(end-begin))