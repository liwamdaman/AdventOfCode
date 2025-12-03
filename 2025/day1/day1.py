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
        return [line.rstrip() for line in lines]

def part1(input):
    print("Part 1: ")
    password = 0
    dial = 50
    for line in input:
        char = line[0]
        steps = int(line[1:])
        if char == 'L':
            dial = (dial - steps) % 100
        elif char == 'R':
            dial = (dial + steps) % 100
        if dial == 0:
            password += 1
        # print(dial)
    print(password)

def part2(input):
    print("\nPart 2: ")
    password = 0
    dial = 50
    for line in input:
        char = line[0]
        steps = int(line[1:])
        if char == 'L':
            if dial == 0:
                temp = 100
            else:
                temp = dial
            if steps >= temp:
                password += 1 + (steps - temp) // 100
            dial = (dial - steps) % 100
        if char == 'R':
            dial += steps
            while dial > 99:
                dial -= 100
                password += 1
                # print("passed 0 on the way to:" + str(dial))
        # print(dial)
    print(password)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)