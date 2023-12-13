import os
from collections import deque

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def possibileNeighboursByShape(coordinates, lines):
    shape = lines[coordinates[0]][coordinates[1]]
    match shape:
        case '|':
            return [(coordinates[0]-1,coordinates[1]), (coordinates[0]+1,coordinates[1])]
        case '-':
            return [(coordinates[0],coordinates[1]-1), (coordinates[0],coordinates[1]+1)]
        case 'L':
            return [(coordinates[0]-1,coordinates[1]), (coordinates[0],coordinates[1]+1)]
        case 'J':
            return [(coordinates[0]-1,coordinates[1]), (coordinates[0],coordinates[1]-1)]
        case '7':
            return [(coordinates[0],coordinates[1]-1), (coordinates[0]+1,coordinates[1])]
        case 'F':
            return [(coordinates[0],coordinates[1]+1), (coordinates[0]+1,coordinates[1])]
        case 'S':
            return [(coordinates[0]-1,coordinates[1]), (coordinates[0]+1,coordinates[1]), (coordinates[0],coordinates[1]-1), (coordinates[0],coordinates[1]+1)]
        case _:
            return []

def withinBounds(coordinates, lines):
    return not (coordinates[0] < 0 or coordinates[0] >= len(lines) or coordinates[1] < 0 or coordinates[1] >= len(lines[0]))

def findStart(lines):
    for i, line in enumerate(lines):
        if (s := line.find('S')) != -1:
            return (i, s)
        
def getConnectedPipes(lines, curr):
    validNeighbours = []
    possibleNeighbours = [node for node in possibileNeighboursByShape(curr, lines) if withinBounds(node, lines)]
    # possible neighbour is considered valid if it is "pointing" towards curr. We check this by seeing if curr is a possible neighbour for the neighbour.
    for neighbour in possibleNeighbours:
        if curr in possibileNeighboursByShape(neighbour, lines):
            validNeighbours.append(neighbour)
    # there should always only be two
    assert len(validNeighbours) == 2
    return validNeighbours

def bfs(lines, start, visited):
    q = deque()
    q.append(start)
    numSteps = -1
    while q:
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            if curr not in visited:
                visited.add(curr)
                # print(curr)
                validNeighbours = getConnectedPipes(lines, curr)
                # should only have two
                q.append(validNeighbours[0])
                q.append(validNeighbours[1])
        numSteps += 1
    return numSteps - 1

def part1(input):
    print("Part 1: ")
    # print(findStart(input)
    visited = set([])
    print(bfs(input, findStart(input), visited))

# Helps determine if we are crossing the loop/polygon when traversing horizontally from the left
def isCrossingHorizontal(lines, node):
    if node[1] == 0 or lines[node[0]][node[1]] in {'|', 'L', 'F'} or (lines[node[0]][node[1]] == 'S' and lines[node[0]][node[1]-1] in {'.', '|', 'J', '7'}):
        return True
    # Special cases below, we are traversing along a continuous boundary of the loop, like L---J or F---7
    if lines[node[0]][node[1]] == 'J':
        idx = node[1]-1
        while lines[node[0]][idx] == '-':
            idx = idx-1
        if lines[node[0]][idx] == 'L':
            # We want to add 1 to count to "reset" the odd/even count, so return True
            return True
    if lines[node[0]][node[1]] == '7':
        idx = node[1]-1
        while lines[node[0]][idx] == '-':
            idx = idx-1
        if lines[node[0]][idx] == 'F' or lines[node[0]][idx] == 'S': # the 'S' check here isn't actually properly sufficient. but we only one S per map so I'll just fix it accordingly to the input 
            # We want to add 1 to count to "reset" the odd/even count, so return True
            return True

def part2(input):
    print("\nPart 2: ")
    visited = set([])
    bfs(input, findStart(input), visited)
    # Clean up all unvisited points
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (i, j) not in visited:
                input[i] = input[i][:j] + '.' + input[i][j + 1:]
    # print(input)
    # Use Ray casting algorithm, see https://en.wikipedia.org/wiki/Point_in_polygon
    pointsInsideLoop = []
    for i in range(len(input)):
        count = 0
        for j in range(len(input[i])):
            if input[i][j] != '.':
                if isCrossingHorizontal(input, (i,j)):
                    count += 1
            elif count % 2 == 1:
                # Odd number of intersections, this point is in the loop
                pointsInsideLoop.append((i,j))
    # print(pointsInsideLoop)
    print(len(pointsInsideLoop))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)