import sys
import os
import collections
import copy
import functools
import re
import itertools
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def exploreRegion(input, i, j, regionId, visited):
    if (i, j) in visited:
        return 0, 0
    visited.add((i, j))
    area = 0
    perimeter = 0
    if i > 0 and input[i - 1][j] == regionId:
        result = exploreRegion(input, i - 1, j, regionId, visited)
        area += result[0]
        perimeter += result[1]
    else:
        perimeter += 1
    if i < len(input) - 1 and input[i + 1][j] == regionId:
        result = exploreRegion(input, i + 1, j, regionId, visited)
        area += result[0]
        perimeter += result[1]
    else:
        perimeter += 1
    if j > 0 and input[i][j - 1] == regionId:
        result = exploreRegion(input, i, j - 1, regionId, visited)
        area += result[0]
        perimeter += result[1]
    else:
        perimeter += 1
    if j < len(input[0]) - 1 and input[i][j + 1] == regionId:
        result = exploreRegion(input, i, j + 1, regionId, visited)
        area += result[0]
        perimeter += result[1]
    else:
        perimeter += 1
    return area + 1, perimeter

def part1(input):
    print("Part 1: ")
    visitedTotal = set()
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            regionId = input[i][j]
            if (i, j) in visitedTotal:
                continue
            visited = set()
            area, perimeter = exploreRegion(input, i, j, regionId, visited)
            visitedTotal.update(visited)
            sum += area * perimeter
            # print("i: {}, j: {}, region: {}, area: {}, perimeter: {}".format(i, j, regionId, area, perimeter))
    print(sum)
        
def exploreRegion2(input, i, j, regionId, visited):
    # num corners = num sides, so count corners
    if (i, j) in visited or i < 0 or j < 0 or i >= len(input) or j >= len(input[0]) or input[i][j] != regionId:
        return 0, 0
    visited.add((i, j))
    area = 0
    corners = 0
    # inside corners
    if i > 0 and input[i - 1][j] == regionId and j > 0 and input[i][j - 1] == regionId and input[i - 1][j - 1] != regionId:
        corners += 1
    if i > 0 and input[i - 1][j] == regionId and j < len(input[0]) - 1 and input[i][j + 1] == regionId and input[i - 1][j + 1] != regionId:
        corners += 1
    if i < len(input) - 1 and input[i + 1][j] == regionId and j > 0 and input[i][j - 1] == regionId and input[i + 1][j - 1] != regionId:
        corners += 1
    if i < len(input) - 1 and input[i + 1][j] == regionId and j < len(input[0]) - 1 and input[i][j + 1] == regionId and input[i + 1][j + 1] != regionId:
        corners += 1
    # outside corners
    if (i > 0 and input[i - 1][j] != regionId or i == 0) and (j > 0 and input[i][j - 1] != regionId or j == 0):
        corners += 1
    if (i > 0 and input[i - 1][j] != regionId or i == 0) and (j < len(input[0]) - 1 and input[i][j + 1] != regionId or j == len(input[0]) - 1):
        corners += 1
    if (i < len(input) - 1 and input[i + 1][j] != regionId or i == len(input) - 1) and (j > 0 and input[i][j - 1] != regionId or j == 0):
        corners += 1
    if (i < len(input) - 1 and input[i + 1][j] != regionId or i == len(input) - 1) and (j < len(input[0]) - 1 and input[i][j + 1] != regionId or j == len(input[0]) - 1):
        corners += 1

    result = exploreRegion2(input, i - 1, j, regionId, visited)
    area += result[0]
    corners += result[1]
    result = exploreRegion2(input, i + 1, j, regionId, visited)
    area += result[0]
    corners += result[1]
    result = exploreRegion2(input, i, j - 1, regionId, visited)
    area += result[0]
    corners += result[1]
    result = exploreRegion2(input, i, j + 1, regionId, visited)
    area += result[0]
    corners += result[1]

    return area + 1, corners

def part2(input):
    print("\nPart 2: ")
    visitedTotal = set()
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            regionId = input[i][j]
            if (i, j) in visitedTotal:
                continue
            visited = set()
            area, sides = exploreRegion2(input, i, j, regionId, visited)
            visitedTotal.update(visited)
            sum += area * sides
            # print("i: {}, j: {}, region: {}, area: {}, sides: {}".format(i, j, regionId, area, sides))
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)