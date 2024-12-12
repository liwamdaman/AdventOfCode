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
        return [[int(x) for x in line.rstrip()] for line in lines]

def hike(input, i, j, visited9s):
    val = input[i][j]
    if val == 9:
        if visited9s == None:
            return 1
        if (i, j) not in visited9s:
            visited9s.add((i, j))
            return 1
        return 0
    score = 0
    if i - 1 >= 0 and input[i - 1][j] == val + 1:
        score += hike(input, i - 1, j, visited9s)
    if j - 1 >= 0 and input[i][j - 1] == val + 1:
        score += hike(input, i, j - 1, visited9s)
    if i + 1 < len(input) and input[i + 1][j] == val + 1:
        score += hike(input, i + 1, j, visited9s)
    if j + 1 < len(input[0]) and input[i][j + 1] == val + 1:
        score += hike(input, i, j + 1, visited9s)
    return score

def part1(input):
    print("Part 1: ")
    numPaths = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                visited9s = set()
                numPaths += hike(input, i, j, visited9s)
                # print("i: {}, j: {}, numPaths: {}".format(i, j, numPaths))
    print(numPaths)

def part2(input):
    print("\nPart 2: ")
    numPaths = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                numPaths += hike(input, i, j, None)
    print(numPaths)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)