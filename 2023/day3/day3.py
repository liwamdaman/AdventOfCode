import os
import re

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines

def getIndicesForPart(part):
    partStartIdx = part[1]
    end = partStartIdx + len(part[0])
    return partStartIdx, end

def isPartNumber(startIndex, endIndex, lineIndex, lines):
    isValid = False
    for i in range(startIndex, endIndex):
        isValid = isValid or hasSymbolAdjacent(i, lineIndex, lines)
    return isValid

def hasSymbolAdjacent(col, row, lines):
    rows = len(lines)
    # treat line as one shorter since newline char
    cols = len(lines[0])-1
    # check row above
    if row != 0:
        if col != 0:
            if lines[row-1][col-1] != '.' and not lines[row-1][col-1].isdigit():
                return True
        if lines[row-1][col] != '.' and not lines[row-1][col].isdigit():
                return True
        if col != cols - 1:
            if lines[row-1][col+1] != '.' and not lines[row-1][col+1].isdigit():
                return True
    # check same row
    if col != 0:
        if lines[row][col-1] != '.' and not lines[row][col-1].isdigit():
            return True
    if col != cols - 1:
        if lines[row][col+1] != '.' and not lines[row][col+1].isdigit():
            return True
    # check next row
    if row != rows - 1:
        if col != 0:
            if lines[row+1][col-1] != '.' and not lines[row+1][col-1].isdigit():
                return True
        if lines[row+1][col] != '.' and not lines[row+1][col].isdigit():
                return True
        if col != cols - 1:
            if lines[row+1][col+1] != '.' and not lines[row+1][col+1].isdigit():
                return True
    return False

def part1(input):
    print("Part 1: ")
    sum = 0
    for i, line in enumerate(input):
        partMatches = list(re.finditer("(\d+)", line))
        parts = [(partMatch.group(), partMatch.start()) for partMatch in partMatches]

        # if len(parts) != len(set(parts)):
        #     print(parts)
        # print(parts)

        for part in parts:
            print(part[0])
            (start, end) = getIndicesForPart(part)
            print((start, end, i))
            print(isPartNumber(start, end, i, input))
            if(isPartNumber(start, end, i, input)):
                sum = sum + int(part[0])
    print(sum)

def processPartForGears(partNumber, startIndex, endIndex, lineIndex, lines, gears):
    sum = 0
    for i in range(startIndex, endIndex):
        adjacentGear = getGearAdjacent(i, lineIndex, lines) 
        if adjacentGear != None:
            # print(adjacentGear)
            if adjacentGear in gears:
                print(gears[adjacentGear])
                print(partNumber)
                sum = sum + gears[adjacentGear] * partNumber
            else:
                gears[adjacentGear] = partNumber
            # print(gears)
            break
    return sum

def getGearAdjacent(col, row, lines):
    rows = len(lines)
    # treat line as one shorter since newline char
    cols = len(lines[0])-1
    # check row above
    if row != 0:
        if col != 0:
            if lines[row-1][col-1] == "*":
                return (row-1, col-1)
        if lines[row-1][col] == "*":
                return (row-1, col)
        if col != cols - 1:
            if lines[row-1][col+1] == "*":
                return (row-1, col+1)
    # check same row
    if col != 0:
        if lines[row][col-1] == "*":
            return (row, col-1)
    if col != cols - 1:
        if lines[row][col+1] == "*":
            return (row, col+1)
    # check next row
    if row != rows - 1:
        if col != 0:
            if lines[row+1][col-1] == "*":
                return (row+1, col-1)
        if lines[row+1][col] == "*":
                return (row+1, col)
        if col != cols - 1:
            if lines[row+1][col+1] == "*":
                return (row+1, col+1)
    return None

def part2(input):
    print("\nPart 2: ")
    sum = 0
    gears = {}
    for i, line in enumerate(input):
        partMatches = list(re.finditer("(\d+)", line))
        parts = [(partMatch.group(), partMatch.start()) for partMatch in partMatches]
        for part in parts:
            (start, end) = getIndicesForPart(part)
            sum = sum + processPartForGears(int(part[0]), start, end, i, input, gears)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)