import sys
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *
import os
from collections import deque

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
def getNext(curr, lines):
    (i, j, direction) = curr
    if direction == 'R':
        if lines[i][j] == '\\':
            return [(i+1,j,'D')]
        if lines[i][j] == '/':
            return [(i-1,j,'U')]
        if lines[i][j] == '|':
            return [(i+1,j,'D'),(i-1,j,'U')]
        return [(i,j+1,'R')]
    if direction == 'L':
        if lines[i][j] == '\\':
            return [(i-1,j,'U')]
        if lines[i][j] == '/':
            return [(i+1,j,'D')]
        if lines[i][j] == '|':
            return [(i+1,j,'D'),(i-1,j,'U')]
        return [(i,j-1,'L')]
    if direction == 'D':
        if lines[i][j] == '\\':
            return [(i,j+1,'R')]
        if lines[i][j] == '/':
            return [(i,j-1,'L')]
        if lines[i][j] == '-':
            return [(i,j+1,'R'),(i,j-1,'L')]
        return [(i+1,j,'D')]
    else:
        if lines[i][j] == '/':
            return [(i,j+1,'R')]
        if lines[i][j] == '\\':
            return [(i,j-1,'L')]
        if lines[i][j] == '-':
            return [(i,j+1,'R'),(i,j-1,'L')]
        return [(i-1,j,'U')]

def valid(next, lines):
    return 0 <= next[0] < len(lines) and 0 <= next[1] < len(lines[0])

def getNumEnergized(lines, start):
    visited = set([])
    # does not contain directions
    energized = set([])
    q = deque()
    q.appendleft(start)
    while q:
        curr = q.popleft()
        visited.add(curr)
        energized.add((curr[0], curr[1]))
        nexts = [x for x in getNext(curr, lines) if valid(x, lines)]
        [q.append(next) for next in nexts if next not in visited]
    # print(len(energized), start)
    return len(energized)

def part1(input):
    print("Part 1: ")
    print(getNumEnergized(input, (0,0,'R')))

def part2(input):
    print("\nPart 2: ")
    maxEnergized = 0
    m, n = len(input), len(input[0])
    for i in range(m):
        maxEnergized = max(maxEnergized, getNumEnergized(input, (i,0,'R')), getNumEnergized(input, (i,n-1,'L')))
    for j in range(n):
        maxEnergized = max(maxEnergized, getNumEnergized(input, (0,j,'D')), getNumEnergized(input, (m-1,j,'U')))
    print(maxEnergized)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
timeFunction(part2, input)