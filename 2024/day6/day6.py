import sys
import os
import collections
import copy
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
sys.setrecursionlimit(10000)
from utils import *

# iterate through NESW
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [[c for c in line.rstrip()] for line in lines]

def isOutOfBounds(input, i, j):
    return True if i < 0 or j < 0 or i >= len(input) or j >= len(input[0]) else False

def move(input, i, j, dir):
    input[i][j] = 'X'
    next = (i + directions[dir][0], j + directions[dir][1])
    if isOutOfBounds(input, next[0], next[1]):
        input[i][j] = 'X'
        return
    if input[next[0]][next[1]] == '#':
        dir = (dir + 1) % 4
        next = (i + directions[dir][0], j + directions[dir][1])
    # print(next)
    move(input, next[0], next[1], dir)
    
def count(input):
    # prettyPrintMatrix(input)
    return sum([len([x for x in line if x == 'X']) for line in input])

def findGuard(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '^':
                return i, j

def part1(input):
    print("Part 1: ")
    i, j = findGuard(input)
    move(input, i, j, 0)
    print(count(input))

def moveAndCheckLoop(input, i, j, dir, visited):
    input[i][j] = dir
    if (i, j, dir) in visited:
        return True
    visited.add((i, j, dir))
    next = (i + directions[dir][0], j + directions[dir][1])
    if isOutOfBounds(input, next[0], next[1]):
        return False
    if input[next[0]][next[1]] == '#':
        dir = (dir + 1) % 4
        next = (i + directions[dir][0], j + directions[dir][1])
        # need to account for corner case, quite literally. See https://www.reddit.com/r/adventofcode/comments/1h7tovg/comment/m0p4uvm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        if input[next[0]][next[1]] == '#':
            dir = (dir + 1) % 4
            next = (i + directions[dir][0], j + directions[dir][1]) 
    return moveAndCheckLoop(input, next[0], next[1], dir, visited)

def part2(input):
    print("\nPart 2: ")
    sum = 0
    i, j = findGuard(input)
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] != '#':
                input[x][y] = '#'
                visited = set()
                if moveAndCheckLoop(input, i, j, 0, visited):
                    sum = sum + 1
                input[x][y] = '.'
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(copy.deepcopy(input))
part2(input)