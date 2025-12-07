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

LINE_STEP = 2

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def find_start(line):
    return line.index('S')

def part1(input):
    print("Part 1: ")
    count = 0
    start = find_start(input[0])
    beamSet = {start}
    for line in input[1:]:
        for i, c in enumerate(line):
            if c == '^':
                if i in beamSet:
                    beamSet.remove(i)
                    count += 1
                    # Assuming the beam doesn't go off the edge, looking at the examples
                    beamSet.add(i-1)
                    beamSet.add(i+1)
    print(count)

def dfs(input, particle, lineIdx, cache):
    if lineIdx == len(input):
        return 1
    if (lineIdx, particle) in cache:
        # print("Cache hit")
        return cache[(lineIdx, particle)]
    count = 0
    split = False
    for i, c in enumerate(input[lineIdx]):
        if c == '^' and i == particle:
            split = True
            count += dfs(input, particle - 1, lineIdx + LINE_STEP, cache)
            count += dfs(input, particle + 1, lineIdx + LINE_STEP, cache)
    if not split:
        count += dfs(input, particle, lineIdx + LINE_STEP, cache)
    cache[(lineIdx, particle)] = count
    return count

def part2(input):
    print("\nPart 2: ")
    start = find_start(input[0])
    count = dfs(input, start, LINE_STEP, {})
    print(count)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)