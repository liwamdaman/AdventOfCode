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
    
def isNodeValid(node):
    return False if node[0] < 0 or node[1] < 0 or node[0] >= len(input) or node[1] >= len(input[0]) else True

## for debugging ##
def printWithAntinodes(input, antinodes):
    matrix = parseLinesToMatrix(input)
    for antinode in antinodes:
        if matrix[antinode[0]][antinode[1]] == '.':
            matrix[antinode[0]][antinode[1]] = '#'
    prettyPrintMatrix(matrix)

def part1(input):
    print("Part 1: ")
    frequencies = {}
    antinodes = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                frequencies.setdefault(input[i][j], []).append((i, j))
    # print(frequencies)
    for freq, locations in frequencies.items():
        pairs = itertools.combinations(locations, 2)
        # print(list(pairs))
        for (n, m) in pairs:
            dy = m[0] - n[0]
            dx = m[1] - n[1]
            antinode1 = (n[0] - dy, n[1] - dx)
            antinode2 = (m[0] + dy, m[1] + dx)
            if isNodeValid(antinode1):
                antinodes.add(antinode1)
            if isNodeValid(antinode2):
                antinodes.add(antinode2)
    # print(antinodes)
    printWithAntinodes(input, antinodes)
    print(len(antinodes))

def part2(input):
    print("\nPart 2: ")
    frequencies = {}
    antinodes = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                frequencies.setdefault(input[i][j], []).append((i, j))
    # print(frequencies)
    for freq, locations in frequencies.items():
        pairs = itertools.combinations(locations, 2)
        # print(list(pairs))
        for (n, m) in pairs:
            dy = m[0] - n[0]
            dx = m[1] - n[1]
            antinode1 = (n[0] - dy, n[1] - dx)
            while isNodeValid(antinode1):
                antinodes.add(antinode1)
                antinode1 = (antinode1[0] - dy, antinode1[1] - dx)
            antinode2 = (m[0] + dy, m[1] + dx)
            while isNodeValid(antinode2):
                antinodes.add(antinode2)
                antinode2 = (antinode2[0] + dy, antinode2[1] + dx)
        antinodes.update(locations)
    # print(antinodes)
    printWithAntinodes(input, antinodes)
    print(len(antinodes))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)