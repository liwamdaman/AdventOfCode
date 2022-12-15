from collections import deque 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def adjacents(self):
        return [Point(self.x-1, self.y), Point(self.x+1, self.y), Point(self.x, self.y-1), Point(self.x, self.y+1)]
    def isValid(self, rows, cols):
        return self.x >= 0 and self.x < cols and self.y >= 0 and self.y < rows

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def parseMap(lines):
    map = []
    start, end = None, None
    for j in range(len(lines)):
        row = []
        for i in range(len(lines[0].rstrip())):
            row.append(lines[j][i])
            if lines[j][i] == 'S':
                start = Point(i, j)
            if lines[j][i] == 'E':
                end = Point(i, j)
        map.append(row)
    return map, start, end

def bfs(map, start, isPart2):
    rows = len(map)
    cols = len(map[0])
    visited = set()
    q = deque([(start, 0)])
    while len(q):
        current = q.popleft()
        if current[0] in visited:
            continue
        if isPart2:
            if height(map[current[0].y][current[0].x]) == height('S'):
                return current[1]
        else:
            if map[current[0].y][current[0].x] == 'E':
                return current[1]
        visited.add(current[0])
        adjacents = current[0].adjacents()
        for adjacent in adjacents:
            if isPart2:
                if adjacent.isValid(rows, cols) and (adjacent not in visited) and (height(map[current[0].y][current[0].x]) - height(map[adjacent.y][adjacent.x]) <= 1):
                    q.append((adjacent, current[1] + 1))
            else:
                if adjacent.isValid(rows, cols) and (adjacent not in visited) and (height(map[adjacent.y][adjacent.x]) - height(map[current[0].y][current[0].x]) <= 1):
                    q.append((adjacent, current[1] + 1))

def height(char):
    if char == 'S':
        return height('a')
    if char == 'E':
        return height('z')
    return ord(char)

def part1(input):
    print("Part 1: ")
    map, start, _ = parseMap(input)
    steps = bfs(map, start, False)
    print(steps)

def part2(input):
    print("\nPart 2: ")
    map, _, end = parseMap(input)
    steps = bfs(map, end, True)
    print(steps)

input = parseInput("input.txt")

part1(input)
part2(input)