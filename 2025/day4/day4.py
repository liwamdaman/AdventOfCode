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
    ROWS = len(input)
    COLS = len(input[0])
    count = 0
    for i in range(ROWS):
        for j in range(COLS):
            if input[i][j] == '@':
                sum = 0
                # print("node: {}, neighbours: {}".format((i,j), list(findNodeNeighbours(input, (i,j)))))
                for node in findNodeNeighbours(input, (i,j)):
                    if input[node[0]][node[1]] == '@':
                        sum += 1
                if sum < 4:
                    # print((i,j))
                    count += 1
    print(count)

def part2(input):
    print("\nPart 2: ")
    input = parseLinesToMatrix(input)
    ROWS = len(input)
    COLS = len(input[0])
    prevCount = -1
    count = 0
    while prevCount != count:
        prevCount = count
        for i in range(ROWS):
            for j in range(COLS):
                if input[i][j] == '@':
                    sum = 0
                    for node in findNodeNeighbours(input, (i,j)):
                        if input[node[0]][node[1]] == '@':
                            sum += 1
                    if sum < 4:
                        count += 1
                        input[i][j] = '.'
    print(count)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)