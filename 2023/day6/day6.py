import os

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def calculateDistance(timeHeldDown, totalTime):
    return (totalTime-timeHeldDown) * timeHeldDown

def getNumWaysToWin(time, distance):
    numWays = 0
    for j in range(time):
        if calculateDistance(j, time) > distance:
            numWays += 1
    return numWays

def part1(input):
    print("Part 1: ")
    times = [int(time) for time in input[0].split(":")[1].split()]
    # print(times)
    distances = [int(distance) for distance in input[1].split(":")[1].split()]
    # print(distances)
    result = 1
    for i, time in enumerate(times):
        result *= getNumWaysToWin(time, distances[i])
    print(result)


def part2(input):
    print("\nPart 2: ")
    time = int(input[0].split(":")[1].replace(' ', ''))
    # print(time)
    distance = int(input[1].split(":")[1].replace(' ', ''))
    # print(distance)
    print(getNumWaysToWin(time, distance))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)