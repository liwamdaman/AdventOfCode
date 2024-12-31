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
        [towels, patterns] = f.read().split('\n\n')
        towels = towels.rstrip().split(', ')
        patterns = [line.rstrip() for line in patterns.split('\n')]
        return towels, patterns

def buildable(towels, pattern):
    for towel in towels:
        if pattern == towel:
            return True
        if pattern[:len(towel)] == towel:
            if buildable(towels, pattern[len(towel):]):
                return True
    return False

def part1(input):
    print("Part 1: ")
    towels, patterns = input
    # print(towels)
    # print(patterns)
    sum = 0
    for pattern in patterns:
        if buildable(towels, pattern):
            sum += 1
    print(sum)

def buildableCount(towels, pattern, cache):
    if pattern in cache:
        return cache[pattern]
    count = 0
    for towel in towels:
        if pattern == towel:
            count += 1
        if pattern[:len(towel)] == towel:
            count += buildableCount(towels, pattern[len(towel):], cache)
    cache[pattern] = count
    return count

def part2(input):
    print("\nPart 2: ")
    towels, patterns = input
    sum = 0
    cache = {}
    for pattern in patterns:
        sum += buildableCount(towels, pattern, cache)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)