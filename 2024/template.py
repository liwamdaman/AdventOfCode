import sys
import os
import collections
import copy
import functools
import re
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def part1(input):
    print("Part 1: ")

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
input = parseInput(filename)

part1(input)
part2(input)