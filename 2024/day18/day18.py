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
    
def getNeighbours(curr, blocked, visited, m):
    (i, j) = curr
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < m:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < m:
        neighbours.append((i, j + 1))
    neighbours = [node for node in neighbours if (node not in blocked and node not in visited)]
    visited.update(neighbours)
    return neighbours

def BFS(blocked, finish, m):
    q = collections.deque()
    visited = set()
    visited.add((0, 0))
    q.append(((0, 0), 0))
    while len(q) > 0:
        curr = q.popleft()
        # print(curr)
        if curr[0] == finish:
            return True, curr[1]
        for node in getNeighbours(curr[0], blocked, visited, m):
            q.append((node, curr[1] + 1))
    return False, 0

def part1(input):
    print("Part 1: ")
    blocked = set()
    numBytes = 1024
    m = 70
    finish = (m, m)
    for line in input[:numBytes]:
        [x, y] = line.split(',')
        blocked.add((int(x), int(y)))
    # print(blocked)
    _, pathLength = BFS(blocked, finish, m)
    print(pathLength)

def part2(input):
    print("\nPart 2: ")
    blocked = set()
    m = 70
    finish = (m, m)
    for line in input:
        [x, y] = line.split(',')
        blocked.add((int(x), int(y)))
        pathExists, pathLength = BFS(blocked, finish, m)
        if not pathExists:
            print(x + ',' + y)
            return

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)