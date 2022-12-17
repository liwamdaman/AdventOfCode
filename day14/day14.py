import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def initializeCave(lines, isPart2=False):
    xMax = 0
    yMax = 0
    for line in lines:
        matches = re.findall('(\d+,\d+)', line.rstrip())
        for match in matches:
            x, y = map(int, match.split(','))
            if x > xMax:
                xMax = x
            if y > yMax:
                yMax = y
    if isPart2:
        # Probably not the best way to do it, but lets just triple xMax and we should be safe 
        xMax = xMax * 3
        cave = [['.' for i in range(xMax+2)] for j in range(yMax+2)]
        cave.append(['#' for i in range(xMax+2)])
        return cave
    return [['.' for i in range(xMax+2)] for j in range(yMax+2)]

def parseRocks(lines, cave):
    for line in lines:
        points = re.findall('(\d+,\d+)', line.rstrip())
        for i in range(len(points)-1):
            x, y = map(int, points[i].split(','))
            xNext, yNext = map(int, points[i+1].split(','))
            # print("{}, {} -> {}, {}".format(x, y, xNext, yNext))
            if x == xNext:
                # Vertical line
                for j in range(min(y, yNext), max(y, yNext) + 1):
                    cave[j][x]='#'
            elif y == yNext:
                # Horizontal line
                for j in range(min(x, xNext), max(x, xNext) + 1):
                    cave[y][j]='#'
            else:
                print('uh oh')

def simulateSand(cave, isPart2=False):
    abyss = len(cave)-1
    count = 0
    while True:
        curr = Point(500, 0)
        while curr != nextMove(curr, cave):
            curr = nextMove(curr, cave)
            if not isPart2 and curr.y == abyss:
                return count
        cave[curr.y][curr.x] = 'o'
        count += 1
        if isPart2 and curr == Point(500, 0):
            return count

def nextMove(sand, cave):
    if cave[sand.y + 1][sand.x] == '.':
        return Point(sand.x, sand.y + 1)
    if cave[sand.y + 1][sand.x - 1] == '.':
        return Point(sand.x - 1, sand.y + 1)
    if cave[sand.y + 1][sand.x + 1] == '.':
        return Point(sand.x + 1, sand.y + 1)
    return sand

## for debugging ##
def printCave(cave):
    for row in cave:
        for i in range(450, 550):
            print(row[i], end="")
        print("")

def part1(input):
    print("Part 1: ")
    cave = initializeCave(input)
    parseRocks(input, cave)
    count = simulateSand(cave)
    print(count)
    # printCave(cave)

def part2(input):
    print("\nPart 2: ")
    cave = initializeCave(input, True)
    parseRocks(input, cave)
    count = simulateSand(cave, True)
    print(count)
    # printCave(cave)

input = parseInput("input.txt")

part1(input)
part2(input)