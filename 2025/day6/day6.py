from ast import parse
import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
import math
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [[x for x in line.rstrip().split()] for line in lines]

def part1(input):
    print("Part 1: ")
    # print(input)
    res = 0
    ROWS = len(input)
    COLS = len(input[0])
    for c in range(COLS):
        nums = []
        for r in range(ROWS-1):
            nums.append(int(input[r][c]))
        operation = input[ROWS-1][c]
        if operation == '+':
            res += sum(nums)
        else:
            res += math.prod(nums)
    print(res)

def parseInput2(filename):
    with open(filename) as f:
        lines = f.readlines()
        lastLine = lines[-1]
        widths = []
        curr = 0
        for c in lastLine[1:]:
            if c == ' ':
                curr += 1
            else:
                widths.append(curr)
                curr = 0
        # append last block of spaces
        widths.append(curr + 1)
        operations = lastLine.split()
        problems = []
        i = 0
        for width in widths:
            problem = []
            for line in lines[:-1]:
                problem.append(line[i:i+width])
            problems.append(problem)
            i += width + 1
        return problems, operations

def part2(filename):
    print("\nPart 2: ")
    problems, operations = parseInput2(filename)
    # print(problems)
    # print(operations)
    res = 0
    for i, problem in enumerate(problems):
        verticalNums = []
        for j in range(len(problem[0])):
            temp = ''
            for num in problem:
                if num[j] != ' ':
                    temp += num[j]
            verticalNums.append(temp)
        # print(verticalNums)
        operation = operations[i]
        verticalNums = [int(x) for x in verticalNums]
        if operation == '+':
            res += sum(verticalNums)
        else:
            res += math.prod(verticalNums)
    print(res)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(filename)