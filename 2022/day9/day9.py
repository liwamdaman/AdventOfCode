class Point:
    def __init__(self, x, y, isTail):
        self.x = x
        self.y = y
        self.isTail = isTail
    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

# Assuming all moves are valid, don't need to check for negative indices
def makeMove(rope, move, visitedSet):
    direction, steps = move.rstrip().split(" ")
    steps = int(steps)
    match direction:
        case 'R':
            for i in range(steps):
                rope[0].x = rope[0].x + 1
                for ropeIndex in range(len(rope)-1):
                    moveAdjacentNode(rope[ropeIndex], rope[ropeIndex+1], visitedSet)
        case 'U':
            for i in range(steps):
                rope[0].y = rope[0].y + 1
                for ropeIndex in range(len(rope)-1):
                    moveAdjacentNode(rope[ropeIndex], rope[ropeIndex+1], visitedSet)
        case 'L':
            for i in range(steps):
                rope[0].x = rope[0].x - 1
                for ropeIndex in range(len(rope)-1):
                    moveAdjacentNode(rope[ropeIndex], rope[ropeIndex+1], visitedSet)
        case 'D':
            for i in range(steps):
                rope[0].y = rope[0].y - 1
                for ropeIndex in range(len(rope)-1):
                    moveAdjacentNode(rope[ropeIndex], rope[ropeIndex+1], visitedSet)
        case _:
            print("uh ohhh")

def moveAdjacentNode(H, T, visitedSet):
    if isFar(H, T):
        if H.x == T.x:
            # Simple movement, move tail to vertical midpoint
            T.y = (H.y + T.y)//2
            if T.isTail:
                visitedSet.add((T.x, T.y))
        elif H.y == T.y:
            # Simple movement, move tail to horizontal midpoint
            T.x = (H.x + T.x)//2
            if T.isTail:
                visitedSet.add((T.x, T.y))
        else:
            # Diagonal movement case
            if abs(H.x - T.x) > 1:
                T.x = (H.x + T.x)//2
                T.y = H.y
            else:
                T.y = (H.y + T.y)//2
                T.x = H.x
            if T.isTail:
                visitedSet.add((T.x, T.y))

def isFar(H, T):
    return abs(H.x - T.x) > 1 or abs(H.y - T.y) > 1

def part1(input):
    print("Part 1: ")
    rope = [Point(0, 0, False), Point(0, 0, True)]
    visitedSet = set()
    visitedSet.add((0,0))
    for line in input:
        makeMove(rope, line, visitedSet)
    print(len(visitedSet))

def part2(input):
    print("\nPart 2: ")
    rope = [Point(0, 0, False) for i in range(9)]
    rope.append(Point(0, 0, True))
    visitedSet = set()
    visitedSet.add((0,0))
    for line in input:
        makeMove(rope, line, visitedSet)
    print(len(visitedSet))

input = parseInput("input.txt")

part1(input)
part2(input)