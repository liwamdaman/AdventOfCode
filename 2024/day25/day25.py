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
        schematics = f.read().split('\n\n')
        return [[line.rstrip() for line in schematic.split('\n')] for schematic in schematics]
    
def countPinHeightsForLock(lock):
    heights = []
    for j in range(len(lock[0])):
        count = 0
        for i in range(1, len(lock)):
            if lock[i][j] == '#':
                count += 1
        heights.append(count)
    return heights

def countHeightsForKey(key):
    heights = []
    for j in range(len(key[0])):
        count = 0
        for i in range(0, len(key) - 1):
            if key[i][j] == '#':
                count += 1
        heights.append(count)
    return heights

def part1(input):
    print("Part 1: ")
    lockHeights = []
    keyHeights = []
    for schematic in input:
        # prettyPrintLines(schematic)
        if schematic[0][0] == '#':
            lockHeights.append(countPinHeightsForLock(schematic))
        else:
            keyHeights.append(countHeightsForKey(schematic))
    # print(lockHeights)
    # print(keyHeights)
    count = 0
    for lock in lockHeights:
        for key in keyHeights:
            count += 1 if all(key[i] <= 5 - lock[i] for i in range(len(key))) else 0
    print(count)

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)