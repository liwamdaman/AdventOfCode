import sys
sys.path.insert(1, '/Users/willi/adventOfCode/utils')

import os
from utils import prettyPrintLines

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
def parsePatterns(input):
    patterns = [[]]
    for line in input:
        if line:
            patterns[-1].append(line)
        else:
            patterns.append([])
    return patterns

def getRotated90CW(lines):
    # Found this on https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    return list(zip(*lines[::-1]))

def getFlippedUpDown(lines):
    return [line for line in reversed(lines)]

def comparelines(lines1, lines2):
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            return False
    return True

def getValue(pattern, originalValue = -1):
    for i in range(1,len(pattern)):
        if comparelines(getFlippedUpDown(pattern[:i]), pattern[i:]):
            if (val := i * 100) == originalValue:
                continue
            else:
                return val
    rotated = getRotated90CW(pattern)
    for i in range(1,len(rotated)):
        if comparelines(getFlippedUpDown(rotated[:i]), rotated[i:]):
            if (val := i) == originalValue:
                continue
            else:
                return val
    return 0

def part1(input):
    print("Part 1: ")
    patterns = parsePatterns(input)
    sum = 0
    for pattern in patterns:
        sum += getValue(pattern)
    print(sum)

def getSmudgedPatterns(pattern):
    smudgedPatterns = []
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            temp = pattern.copy()
            temp[i] = temp[i][:j] + '.' + temp[i][j+1:] if temp[i][j] == '#' else temp[i][:j] + '#' + temp[i][j+1:]
            smudgedPatterns.append(temp)
    return smudgedPatterns

def part2(input):
    print("\nPart 2: ")
    patterns = parsePatterns(input)
    sum = 0
    for pattern in patterns:
        # Brute force this shit baby
        originalValue = getValue(pattern)
        for smudgedPattern in getSmudgedPatterns(pattern):
            if (val := getValue(smudgedPattern, originalValue)) != 0:
                sum += val
                break
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)