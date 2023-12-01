def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def process(input, perCycleFunc, output):
    cycle = 1
    X = 1
    for line in input:
        line = line.rstrip()
        if line == "noop":
            perCycleFunc(output, cycle, X)
            cycle += 1
        else:
            # addx
            n = int(line.split(" ")[1])
            perCycleFunc(output, cycle, X)
            cycle += 1
            perCycleFunc(output, cycle, X)
            cycle += 1
            X += n

## For part 1 ##
def incrementSignalStrengthIfNeeded(signalStrength, cycle, X):
    if cycle % 40 == 20:
        signalStrength[0] += cycle * X
################

## For part 2 ##
def drawPixel(buffer, cycle, X):
    rowPos = (cycle-1) % 40
    if rowPos == X or rowPos == X - 1 or rowPos == X + 1:
        buffer.append('#')
    else:
        buffer.append('.')

def render(buffer):
    for i in range(len(buffer)):
        if i % 40 == 0:
            print('\n', end="")
        print(buffer[i], end="")
################

def part1(input):
    print("Part 1: ")
    signalStrength = [0]
    process(input, incrementSignalStrengthIfNeeded, signalStrength)
    print(signalStrength[0])

def part2(input):
    print("\nPart 2: ")
    CrtBuffer = []
    process(input, drawPixel, CrtBuffer)
    render(CrtBuffer)

input = parseInput("input.txt")

part1(input)
part2(input)