import os

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines
    
def extrapolate(line):
    line = [int(x) for x in line.split()]
    lastVals = []
    lastVals.append(line[-1])
    diffs = nextDifference(line)
    lastVals.append(diffs[-1])
    while not isAllZeroes(diffs):
        diffs = nextDifference(diffs)
        lastVals.append(diffs[-1])
    return sum(lastVals)

def extrapolateFirst(line):
    line = [int(x) for x in line.split()]
    firstVals = []
    firstVals.append(line[0])
    diffs = nextDifference(line)
    firstVals.append(diffs[0])
    while not isAllZeroes(diffs):
        diffs = nextDifference(diffs)
        firstVals.append(diffs[0])
    firstVals = list(reversed(firstVals))
    res = firstVals[1] - firstVals[0]
    for val in firstVals[2:]:
        res = val - res
    return res

def nextDifference(vals):
    diffs = []
    for i, x in enumerate(vals):
        if i == 0:
            continue
        diffs.append(x - vals[i-1])
    return diffs

def isAllZeroes(vals):
    return len([val for val in vals if val != 0]) == 0

def part1(input):
    print("Part 1: ")
    print(sum([extrapolate(line) for line in input]))

def part2(input):
    print("\nPart 2: ")
    print(sum([extrapolateFirst(line) for line in input]))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)