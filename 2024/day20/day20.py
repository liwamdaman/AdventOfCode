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

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def findStart(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                return i, j
            
def findEnd(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'E':
                return i, j

def getNeighbours(input, curr, visited):
    (i, j) = curr
    # No need to check index bounds, since walls all around
    all = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    neighbours = [node for node in all if (input[node[0]][node[1]] != '#' and node not in visited)]
    visited.update(neighbours)
    return neighbours

def BFS(input, S, E, distanceFromStart):
    q = collections.deque()
    visited = set()
    q.append((S, 0))
    visited.add(S)
    while len(q) > 0:
        curr = q.popleft()
        distanceFromStart[curr[0]] = curr[1]
        if curr[0] == E:
            return
        neighbours = getNeighbours(input, curr[0], visited)
        # Should only have one since maze only has one path, this isn't really BFS
        assert len(neighbours) == 1
        q.append((neighbours[0], curr[1] + 1))

def manhattanDistance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def solve(input, cheatLengthMax, minimumSave):
    S = findStart(input)
    E = findEnd(input)
    # THERES ONLY ONE PATH, NO BRANCHING IN MAZE
    distanceFromStart = {}
    BFS(input, S, E, distanceFromStart)
    count = 0
    for node, distance in distanceFromStart.items():
        (x, y) = node
        for i in range(x - cheatLengthMax, x + cheatLengthMax + 1):
            for j in range(y - cheatLengthMax, y + cheatLengthMax + 1):
                if i >= 0 and i < len(input) and j >= 0 and j < len(input[0]) and manhattanDistance(node, (i, j)) <= cheatLengthMax and (i, j) in distanceFromStart and distanceFromStart[(i, j)] - distance - manhattanDistance(node, (i, j)) >= minimumSave:
                    count += 1
                    # print("cheat from {} to {}, saving {} picoseconds".format(node, (i, j), distanceFromStart[(i, j)] - distance - manhattanDistance(node, (i, j))))
    return count

def part1(input):
    print("Part 1: ")
    cheatLengthMax = 2
    minimumSave = 100
    print(solve(input, cheatLengthMax, minimumSave))

def part2(input):
    print("\nPart 2: ")
    cheatLengthMax = 20
    minimumSave = 100
    print(solve(input, cheatLengthMax, minimumSave))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)