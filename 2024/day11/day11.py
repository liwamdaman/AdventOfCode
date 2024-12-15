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
        return f.readline().rstrip().split()
    
def blink(input):
    output = []
    for stone in input:
        output.extend(applyRule(stone))
    return output

def applyRule(stone):
    if stone == '0':
        return ['1']
    if (len(stone) % 2) == 0:
        return [stone[:(len(stone) // 2)], str(int(stone[(len(stone) // 2):]))]
    return [str(int(stone) * 2024)]

def part1(input):
    print("Part 1: ")
    for i in range(25):
        input = blink(input)
        # print(input)
    print(len(input))

def blink2(dict):
    output = {}
    for stone, count in dict.items():
        for s in applyRule(stone):
            output[s] = output.get(s, 0) + count
    return output

def part2(input):
    print("\nPart 2: ")
    dict = collections.Counter(input)
    for i in range(75):
        dict = blink2(dict)
    sum = 0
    for stone, count in dict.items():
        sum += count
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)