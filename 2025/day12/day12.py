import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
import math
sys.setrecursionlimit(10000)
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from utils import *
from dataclasses import dataclass

@dataclass
class Region:
    M: int
    N: int
    counts: list[int]

    def buildRegionMatrix(self):
        matrix = [['.' for _ in range(self.M)] for _ in range(self.N)]
        return matrix

def parseInput(filename):
    with open(filename) as f:
        input = f.read().split('\n\n')
        presents = input[:-1]
        presents = [present.split(':\n')[1].split('\n') for present in presents]
        regions = input[-1]
        regions = [region.split(': ') for region in regions.split('\n')]
        regions = [Region(int(size.split('x')[0]), int(size.split('x')[1]), \
            [int(count) for count in counts.split(' ')]) for size, counts in regions]
        return presents, regions

def getPresentsToFit(presents, region):
    presentsToFit = []
    for idx, count in enumerate(region.counts):
        if count > 0:
            for _ in range(count):
                presentsToFit.append(presents[idx]) 
    return presentsToFit

## We always assume the present is size 3x3
def canPlacePresent(matrix, present, i, j):
    for r in range(3):
        for c in range(3):
            if present[r][c] == '#' and matrix[i + r][j + c] == '#':
                return False
    return True

## We always assume the present is size 3x3
def placePresent(matrix, present, i, j):
    for r in range(3):
        for c in range(3):
            if present[r][c] == '#':
                matrix[i + r][j + c] = '#'
    return True

def getOrientations(present):
    orientations = []
    current = present
    for _ in range(4):
        orientations.append(current)
        current = getRotated90CWLines(current)
    # Also add flipped version
    flipped = [row[::-1] for row in present]
    for _ in range(4):
        orientations.append(flipped)
        flipped = getRotated90CWLines(flipped)
    return orientations

def getOpenSpots(matrix):
    res = []
    for r in range(0, len(matrix) - 2):
        for c in range(0, len(matrix[0]) - 2):
            # if matrix[r][c] == '.': # Trying something out, skip this check for now
                res.append((r, c))
    return res

def dfs(matrix, presents, idx):
    # prettyPrintMatrix(matrix)
    # time.sleep(1)
    if idx == len(presents):
        return True
    present = presents[idx]
    placementOptions = itertools.product(getOpenSpots(matrix), getOrientations(present))
    for (i, j), presentRotated in placementOptions:
        if canPlacePresent(matrix, presentRotated, i, j):
            cpy = copy.deepcopy(matrix)
            placePresent(cpy, presentRotated, i, j)
            if dfs(cpy, presents, idx + 1):
                return True
    return False

def part1(input):
    print("Part 1: ")
    presents, regions = input
    res = 0
    for region in regions:
        presentsToFit = getPresentsToFit(presents, region)
        matrix = region.buildRegionMatrix()
        feasible = dfs(matrix, presentsToFit, 0)
        res += 1 if feasible else 0
    print(res)

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
input = parseInput(filename)

part1(input)
part2(input)