import sys
import copy

sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

import os

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
def getLoad(matrix):
    load = 0
    for i, line in enumerate(reversed(matrix)):
        for x in line:
            if x == 'O':
                load += i + 1
    return load

def tiltNorth(matrix):
    for i, line in enumerate(matrix):
        for j, x in enumerate(line):
            if x == 'O':
                if len(above := getAbove(matrix, i, j)) != 0:
                    # print(above)
                    try:
                        numFreeSpaces = [i for i, spot in enumerate(above) if spot in 'O#'][0]
                    except:
                        numFreeSpaces = len(above)
                    # print(numFreeSpaces)
                    if numFreeSpaces > 0:
                        matrix[i-numFreeSpaces][j] = 'O'
                        matrix[i][j] = '.'

def getAbove(matrix, i, j):
    return [line[j] for line in reversed(matrix[:i])]

def part1(input):
    print("Part 1: ")
    rocks = parseLinesToMatrix(input)
    tiltNorth(rocks)
    # prettyPrintMatrix(rocks)
    print(getLoad(rocks))

def cycle(matrix):
    tiltNorth(matrix)
    rotated = getRotated90CWMatrix(matrix)
    tiltNorth(rotated)
    rotated = getRotated90CWMatrix(rotated)
    tiltNorth(rotated)
    rotated = getRotated90CWMatrix(rotated)
    tiltNorth(rotated)
    rotated = getRotated90CWMatrix(rotated)
    return rotated

def matrixToTuple(matrix):
    return tuple([tuple(line) for line in matrix])

def part2(input):
    print("\nPart 2: ")
    rocks = parseLinesToMatrix(input)
    count1 = 0
    seen = set([])
    curr = rocks
    seen.add(matrixToTuple(curr))
    while matrixToTuple(curr := cycle(curr)) not in seen:
        count1 += 1
        seen.add(matrixToTuple(curr))
    # There is a cycle starting at curr. Go again, this time starting at curr and counting
    # print(count1)
    loopStart = copy.deepcopy(curr)
    # prettyPrintMatrix(loopStart)
    count2 = 0
    seen = set([])
    seen.add(matrixToTuple(curr))
    while matrixToTuple(curr := cycle(curr)) not in seen:
        count2 += 1
        seen.add(matrixToTuple(curr))
    # print(count2)
    remainder = (1000000000-(count1-count2)) % (count2+1)
    # print(remainder)
    # prettyPrintMatrix(loopStart)
    for i in range(remainder):
        loopStart = cycle(loopStart)
    prettyPrintMatrix(loopStart)
    print(getLoad(loopStart))


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)