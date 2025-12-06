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
        intervals, numbers = f.read().split('\n\n')
        intervals = intervals.split('\n')
        intervals = [(int(interval.split('-')[0]), int(interval.split('-')[1])) for interval in intervals]
        numbers = [int(number) for number in numbers.split('\n')]
        return intervals, numbers

def part1(input):
    print("Part 1: ")
    count = 0
    intervals, numbers = input
    for number in numbers:
        for interval in intervals:
            if int(interval[0] <= number <= interval[1]):
                count += 1
                break
    print(count)

# Initial thoughts: use set to track all valid id, but this will take too much memory. Instead, use merge interval approach
def part2(input):
    print("\nPart 2: ")
    count = 0
    intervals, _ = input
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    for interval in merged:
        count += interval[1] - interval[0] + 1
    print(count)
    

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)