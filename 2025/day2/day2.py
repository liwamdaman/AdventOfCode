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
        return lines[0].rstrip().split(",")

def isInvalidId(id):
    if len(id) % 2 != 0:
        return False
    mid = len(id) // 2
    return id[:mid] == id[mid:]

# One common method involves concatenating the string with itself and searching for the 
# original string within the concatenated version, starting from the second character.
def isInvalidId2clever(id):
    s = id + id
    return s.find(id, 1) != len(id)

def process(input, isInvalidFn):
    sum = 0
    for interval in input:
        [start, end] = interval.split("-")
        for n in range(int(start), int(end) + 1):
            if isInvalidFn(str(n)):
                # print(n)
                sum += n
    print(sum)

def part1(input):
    print("Part 1: ")
    process(input, isInvalidId)

def part2(input):
    print("\nPart 2: ")
    process(input, isInvalidId2clever)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)