import sys
import os
import collections
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

list1 = []
list2 = []

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            both = line.rstrip().split()
            list1.append(int(both[0]))
            list2.append(int(both[1]))

def part1(input):
    print("Part 1: ")
    list1.sort()
    list2.sort()
    sum = 0
    for i, val in enumerate(list1):
        distance = abs(list2[i] - val)
        sum = sum + distance
    print(sum)

def part2(input):
    print("\nPart 2: ")
    counts = collections.Counter(list2)
    sum = 0
    for v in list1:
        sum = sum + v * counts[v]
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
input = parseInput(filename)

part1(input)
part2(input)