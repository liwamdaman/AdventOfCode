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
    
def operate(i, nums, curVal, val):
    if curVal == val and i == len(nums):
        return True
    if curVal > val or i >= len(nums):
        return False
    return operate(i + 1, nums, curVal + nums[i], val) or operate(i + 1, nums, curVal * nums[i], val)

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        [val, nums] = line.split(": ")
        val = int(val)
        nums = [int(n) for n in nums.split()]
        # print(val)
        # print(nums)
        if operate(1, nums, nums[0], val):
            # print(line)
            sum = sum + val
    print(sum)

def operatePart2(i, nums, curVal, val):
    if curVal == val and i == len(nums):
        return True
    if curVal > val or i >= len(nums):
        return False
    return operatePart2(i + 1, nums, curVal + nums[i], val) or operatePart2(i + 1, nums, curVal * nums[i], val) or operatePart2(i + 1, nums, int(str(curVal) + str(nums[i])), val)

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for line in input:
        [val, nums] = line.split(": ")
        val = int(val)
        nums = [int(n) for n in nums.split()]
        if operatePart2(1, nums, nums[0], val):
            # print(line)
            sum = sum + val
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)