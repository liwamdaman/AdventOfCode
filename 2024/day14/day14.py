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
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def parsePandV(line):
    pos = tuple(map(int, re.findall(r"p=(\d+),(\d+)", line)[0]))
    vel = tuple(map(int, re.findall(r"v=(-*\d+),(-*\d+)", line)[0]))
    # print(pos)
    # print(vel)
    return pos, vel

def score(matrix, height, width):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(0, height // 2):
        for j in range(0, width // 2):
            q1 += matrix[i][j]
    for i in range(0, height // 2):
        for j in range(width // 2 + 1, width):
            q2 += matrix[i][j]
    for i in range(height // 2 + 1, height):
        for j in range(0, width // 2):
            q3 += matrix[i][j]
    for i in range(height // 2 + 1, height):
        for j in range(width // 2 + 1, width):
            q4 += matrix[i][j]
    # # Tree might have bigger difference in quadrant scores instead of seemingly random distribution
    # if max(q1, q2, q3, q4) - min(q1, q2, q3, q4) >= 100:
    #     prettyPrintMatrix(matrix)
    return q1 * q2 * q3 * q4


def part1(input):
    print("Part 1: ")
    numSeconds = 100
    width = 101
    height = 103
    result = [[0 for x in range(width)] for y in range(height)]
    for line in input:
        pos, vel = parsePandV(line)
        # somehow with the magic of modulo this works for negative velocity as well
        newX = (pos[0] + vel[0] * numSeconds) % width
        newY = (pos[1] + vel[1] * numSeconds) % height
        # print((newX, newY))
        result[newY][newX] += 1
    # prettyPrintMatrix(result)
    print(score(result, height, width))

def part2(input):
    print("\nPart 2: ")
    numSeconds = 10000
    width = 101
    height = 103
    for seconds in range(numSeconds):
        result = [[0 for x in range(width)] for y in range(height)]
        for line in input:
            pos, vel = parsePandV(line)
            # somehow with the magic of modulo this works for negative velocity as well
            newX = (pos[0] + vel[0] * seconds) % width
            newY = (pos[1] + vel[1] * seconds) % height
            result[newY][newX] += 1
        # Hint: Tree has no overlaps
        if not any([any([x > 1 for x in line]) for line in result]):
            prettyPrintMatrix(result)
            print(seconds)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)