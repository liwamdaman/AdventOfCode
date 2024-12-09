import sys
import os
import collections
import re
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def findRegexMatches(input):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, input)
    # print(matches)
    return matches

def parseFactors(statement):
    # print([int(x) for x in re.findall(r"\d+", statement)])
    return [int(x) for x in re.findall(r"\d+", statement)]

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        matches = findRegexMatches(line)
        for match in matches:
            factors = parseFactors(match)
            sum = sum + factors[0] * factors[1]
    print(sum)

def findRegexMatchesPart2(input):
    pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    matches = re.findall(pattern, input)
    # print(matches)
    return matches

def part2(input):
    print("\nPart 2: ")
    sum = 0
    enabled = True
    for line in input:
        matches = findRegexMatchesPart2(line)
        for match in matches:
            if match == "don't()":
                enabled = False
            elif match == "do()":
                enabled = True
            elif enabled == True:
                factors = parseFactors(match)
                sum = sum + factors[0] * factors[1]
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)