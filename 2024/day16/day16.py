import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

directionSymbols = [
    '^',
    '>',
    'v',
    '<'
]

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
def findStart(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                return (i, j)

def getPossibleMoves(input, i, j, dir, cost, visited):
    moves = []
    # Straight
    y, x = i + directions[dir][0], j + directions[dir][1]
    if ((y, x, dir) not in visited or visited[(y, x, dir)] >= cost + 1) and input[y][x] != '#':
        moves.append((y, x, dir, cost + 1))
        visited[(y, x, dir)] = cost + 1
    # Turn CW
    if (i, j, (dir + 1) % 4) not in visited or visited[(i, j, (dir + 1) % 4)] >= cost + 1000:
        moves.append((i, j, (dir + 1) % 4, cost + 1000))
        visited[(i, j, (dir + 1) % 4)] = cost + 1000
    # Turn CCW
    if (i, j, (dir - 1) % 4) not in visited or visited[(i, j, (dir - 1) % 4)] >= cost + 1000:
        moves.append((i, j, (dir - 1) % 4, cost + 1000))
        visited[(i, j, (dir - 1) % 4)] = cost + 1000
    return moves

def compareCost(first, second):
    if first[3] < second[3]:
        return -1
    if first[3] > second[3]:
        return 1
    return 0

def printPath(input, path):
    output = [[c for c in line] for line in input]
    for (i, j, dir) in path:
        output[i][j] = directionSymbols[dir]
    prettyPrintMatrix(output)

def part1(input):
    print("Part 1: ")
    i, j = findStart(input)
    visited = {}
    heap = []
    heapq.heappush(heap, (0, (i, j, 1, [])))
    while True:
        cost, (i, j, dir, path) = heapq.heappop(heap)
        if input[i][j] == 'E':
            print(cost)
            # print(path)
            # printPath(input, path)
            return
        for (y, x, newDir, newCost) in getPossibleMoves(input, i, j, dir, cost, visited):
            pathCopy = copy.deepcopy(path)
            pathCopy.append((i, j, dir))
            heapq.heappush(heap, (newCost, (y, x, newDir, pathCopy)))

def printSeats(input, seats):
    output = [[c for c in line] for line in input]
    for (i, j) in seats:
        output[i][j] = 'O'
    prettyPrintMatrix(output)

def part2(input):
    print("\nPart 2: ")
    i, j = findStart(input)
    visited = {}
    heap = []
    bestScore = sys.maxsize
    bestPaths = []
    heapq.heappush(heap, (0, (i, j, 1, [])))
    while True:
        cost, (i, j, dir, path) = heapq.heappop(heap)
        if input[i][j] == 'E':
            if cost > bestScore:
                break
            else:
                bestScore = cost
                bestPaths.append(path)
        for (y, x, newDir, newCost) in getPossibleMoves(input, i, j, dir, cost, visited):
            pathCopy = copy.deepcopy(path)
            pathCopy.append((i, j, dir))
            heapq.heappush(heap, (newCost, (y, x, newDir, pathCopy)))
    seats = set()
    for path in bestPaths:
        for (i, j, dir) in path:
            seats.add((i, j))
    print(len(seats) + 1) # plus one for End tile
    # printSeats(input, seats)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)