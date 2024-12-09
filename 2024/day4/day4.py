import sys
import os
import collections
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

target = "XMAS"

def checkDirection(input, i, j, x, y, next):
    if next == len(target):
        return True
    if i + x < 0 or j + y < 0 or i + x >= len(input) or j + y >= len(input[0]):
        return False
    if input[i + x][j + y] != target[next]:
        return False
    return checkDirection(input, i + x, j + y, x, y, next + 1)


def checkAround(input, i, j):
    sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if checkDirection(input, i, j, x, y, 1):
                sum = sum + 1
    # print("sum: {} i: {} j: {}".format(sum, i, j))
    return sum

def part1(input):
    print("Part 1: ")
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'X':
                sum = sum + checkAround(input, i, j)
    print(sum)

def check(input, i, j):
    if input[i-1][j-1] == 'M' and input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S' and input[i+1][j+1] == 'S':
        return True
    if input[i-1][j-1] == 'S' and input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S' and input[i+1][j+1] == 'M':
        return True
    if input[i-1][j-1] == 'S' and input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M' and input[i+1][j+1] == 'M':
        return True
    if input[i-1][j-1] == 'M' and input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M' and input[i+1][j+1] == 'S':
        return True
    else:
        return False

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if input[i][j] == 'A' and check(input, i, j):
                sum = sum + 1
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)