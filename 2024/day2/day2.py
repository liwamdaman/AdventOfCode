import sys
import os
import collections
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [[int(x) for x in line.rstrip().split()] for line in lines]
    
def isMonotonic(report):
    # print(all([x < y for (x, y) in zip(report, report[1:])]) or all([x > y for (x, y) in zip(report, report[1:])]))
    return all([x < y for (x, y) in zip(report, report[1:])]) or all([x > y for (x, y) in zip(report, report[1:])])

def noBigJumps(report):
    return all([abs(x - y) <= 3 for (x, y) in zip(report, report[1:])])

def isReportValid(report):
    return isMonotonic(report) and noBigJumps(report)

def part1(input):
    print("Part 1: ")
    sum = 0
    for report in input:
        sum = sum + (1 if isReportValid(report) else 0)
    print(sum)

def permutations(report):
    return [report[:i] + report[i+1:] for i, val in enumerate(report)]

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for report in input:
        sum = sum + (1 if any([isReportValid(permutation) for permutation in permutations(report)]) else 0)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)