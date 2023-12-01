def parseInput(filename):
    map = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = []
            for c in line.rstrip():
                row.append(int(c))
            map.append(row)
    return map

## PART 1 FUNCTIONS ##
def createVisibilityMap(map):
    x = len(map[0])
    y = len(map)
    visibilityMap = [[0 for col in range(x)] for row in range(y)]
    return visibilityMap

def left(map, visibilityMap):
    x = len(map[0])
    y = len(map)
    for j in range(y):
        maxHeight = -1
        for i in range(x):
            if map[j][i] > maxHeight:
                visibilityMap[j][i] = 1
                maxHeight = map[j][i]

def right(map, visibilityMap):
    x = len(map[0])
    y = len(map)
    for j in range(y):
        maxHeight = -1
        for i in reversed(range(x)):
            if map[j][i] > maxHeight:
                visibilityMap[j][i] = 1
                maxHeight = map[j][i]

def top(map, visibilityMap):
    x = len(map[0])
    y = len(map)
    for i in range(x):
        maxHeight = -1
        for j in range(y):
            if map[j][i] > maxHeight:
                visibilityMap[j][i] = 1
                maxHeight = map[j][i]

def bottom(map, visibilityMap):
    x = len(map[0])
    y = len(map)
    for i in range(x):
        maxHeight = -1
        for j in reversed(range(y)):
            if map[j][i] > maxHeight:
                visibilityMap[j][i] = 1
                maxHeight = map[j][i]
## PART 1 FUNCTIONS END ##

## PART 2 FUNCTIONS ##
def scoreTreeLeft(i, j, map, height):
    if i == 0:
        return 0
    if height <= map[j][i-1]:
        return 1
    return 1 + scoreTreeLeft(i-1, j, map, height)

def scoreTreeRight(i, j, map, height):
    if i == len(map[0]) - 1:
        return 0
    if height <= map[j][i+1]:
        return 1
    return 1 + scoreTreeRight(i+1, j, map, height)

def scoreTreeUp(i, j, map, height):
    if j == 0:
        return 0
    if height <= map[j-1][i]:
        return 1
    return 1 + scoreTreeUp(i, j-1, map, height)

def scoreTreeDown(i, j, map, height):
    if j == len(map) - 1:
        return 0
    if height <= map[j+1][i]:
        return 1
    return 1 + scoreTreeDown(i, j+1, map, height)
## PART 2 FUNCTIONS END ##

def part1(input):
    print("Part 1: ")
    visibilityMap = createVisibilityMap(input)
    left(input, visibilityMap)
    right(input, visibilityMap)
    top(input, visibilityMap)
    bottom(input, visibilityMap)
    count = 0
    for row in visibilityMap:
        for isVisibile in row:
            if isVisibile:
                count += 1
    print(count)

def part2(input):
    print("\nPart 2: ")
    x = len(input[0])
    y = len(input)
    maxScore = -1
    for j in range(y):
        for i in range(x):
            score = scoreTreeLeft(i, j, input, input[j][i]) * scoreTreeRight(i, j, input, input[j][i]) * scoreTreeUp(i, j, input, input[j][i]) * scoreTreeDown(i, j, input, input[j][i])
            if score > maxScore:
                maxScore = score
    print(maxScore)

input = parseInput("input.txt")

part1(input)
part2(input)