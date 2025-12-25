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

def canPresentAreaFit(presentList, region):
    return presentAreaSum(presentList) <= region.N * region.M

def presentAreaSum(presentList):
    return sum(row.count('#') for present in presentList for row in present)

def can3x3SpacesFit(presentList, region):
    return 9 * len(presentList) <= region.N * region.M

## This problem is NP hard, can't just solve it quickly. Turns out this problem is a bit of gimmick,
## specifically with the input given. Using logic with areas to eliminate or confirm solutions works on the input.
## Annoyingly, this gimmick only works for the input given, and not even for the demo test case.
def part1(input):
    print("Part 1: ")
    presents, regions = input
    res = 0
    for region in regions:
        presentsToFit = getPresentsToFit(presents, region)
        if can3x3SpacesFit(presentsToFit, region):
            res += 1
        elif not canPresentAreaFit(presentsToFit, region):
            continue
        else:
            print("In-between case, uh oh")
    print(res)

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)