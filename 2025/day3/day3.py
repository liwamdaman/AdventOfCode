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
    sum = 0
    for bank in input:
        firstDigit = ''
        secondDigit = ''
        firstIdx = [-1] * 10
        lastIdx = [-1] * 10
        for i, c in enumerate(bank):
            if firstIdx[int(c)] == -1:
                firstIdx[int(c)] = i
            lastIdx[int(c)] = i
        for i in range(9, -1, -1):
            if firstIdx[i] != -1 and firstIdx[i] < len(bank) - 1:
                firstDigit = i
                break
        for i in range(9, -1, -1):
            if lastIdx[i] != -1 and lastIdx[i] > firstIdx[int(firstDigit)]:
                secondDigit = i
                break
        joltage = str(firstDigit) + str(secondDigit)
        # print(joltage)
        sum += int(joltage)
    print(sum)

# # initial intuition, use backtracking/dfs approach to build up all possible permutations of 12 digit numbers
# def part2(input):
#     print("\nPart 2: ")
#     def backtrack(bank, curr, idx, permutations):
#         if len(curr) == 12:
#             permutations.append(curr)
#             return
#         if idx >= len(bank):
#             return
#         backtrack(bank, curr + bank[idx], idx + 1, permutations)
#         backtrack(bank, curr, idx + 1, permutations)
#     sum = 0
#     for bank in input:
#         print("processing bank: " + bank)
#         permutations = []
#         backtrack(bank, '', 0, permutations)
#         sum += max([int(p) for p in permutations])
#     print(sum)

# Next approach, using modified search window 12 times
def part2(input):
    print("\nPart 2: ")
    sum = 0
    for bank in input:
        joltage = ''
        l = 0
        for i in range(11, -1, -1):
            r = len(bank) - i
            window = bank[l:r]
            max_value = max(window)
            max_index = window.index(max_value) + l
            joltage += max_value
            l = max_index + 1
        #     print("window: " + window + ", max value in window: " + max_value + ", index: " + str(max_index))
        # print(joltage)
        sum += int(joltage)
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)