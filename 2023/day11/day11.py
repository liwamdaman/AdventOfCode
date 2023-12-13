import os
from itertools import combinations

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
# Consider adding this to template or accessible utils lib
def prettyPrint(matrix):
    for row in matrix:
        for c in row:
            print(c, end="")
        print()

### PART 1 ###

def expand(lines):
    m = len(lines)
    n = len(lines[0])
    output = []
    emptyRows = set(range(m))
    emptyCols = set(range(n))
    for i, line in enumerate(lines):
        output.append([])
        for j, c in enumerate(line):
            if c == '#':
                emptyRows.discard(i)
                emptyCols.discard(j)
            output[i].append(c)
    # print(emptyRows)
    # print(emptyCols)
    # print(output)

    # Add columns first
    for row in output:
        for i in reversed(range(len(row))):
            if i in emptyCols:
                row.insert(i, '.')
    # Add rows
    n = len(output[0])
    for i in reversed(range(len(output))):
        if i in emptyRows:
            output.insert(i, ['.' for i in range(n)])
    return output

##############

### PART 2 ###

def getExpandedGalaxyLocations(lines, expansionFactor):
    locations = getGalaxyLocations(lines)
    # get empty row and col indexes still
    m = len(lines)
    n = len(lines[0])
    emptyRows = set(range(m))
    emptyCols = set(range(n))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                emptyRows.discard(i)
                emptyCols.discard(j)
    # apply expansion to galaxy locations
    emptyRows = list(emptyRows)
    emptyRows.sort()
    emptyCols = list(emptyCols)
    emptyCols.sort()
    newLocations = []
    for location in locations:
        newRow = location[0]
        newCol = location[1]
        for r in reversed(emptyRows):
            if r < newRow:
                newRow = newRow + expansionFactor-1
        for c in reversed(emptyCols):
            if c < newCol:
                newCol = newCol + expansionFactor-1
        newLocations.append((newRow, newCol))
    # print(newLocations)
    return newLocations

##############

def getGalaxyLocations(matrix):
    locations = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                locations.append((i,j))
    return locations

def getShortestPathSteps(start, end):
    # just calculate manhattan distance
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def computeCombinations(locations):
    galaxyCombinations = combinations(locations, 2)
    sum = 0
    for comb in galaxyCombinations:
        sum += getShortestPathSteps(comb[0], comb[1])
    print(sum)


def part1(input):
    print("Part 1: ")
    expanded = expand(input)
    # prettyPrint(expanded)
    locations = getGalaxyLocations(expanded)
    computeCombinations(locations)


def part2(input):
    print("\nPart 2: ")
    locations = getExpandedGalaxyLocations(input, 1000000)
    computeCombinations(locations)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)