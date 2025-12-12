from operator import indexOf
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
        res = []
        for line in lines:
            line = line.rstrip()
            i = indexOf(line, ']')
            j = indexOf(line, '{')
            goal = line[:i+1]
            buttons = line[i+2:j-1].split()
            joltages = line[j:]
            res.append((goal, buttons, joltages))
        return res

def parseGoal(goal):
    return int(goal[1:-1].replace('.', '0').replace('#', '1')[::-1], 2)

def parseButtons(buttons):
    return [[1 << int(d) for d in button[1:-1].split(',')] for button in buttons]

def applyButton(button, state):
    res = state
    for light in button:
        res ^= light
    return res

def bfs(goal, buttons):
    q = collections.deque([(button, 0, 0) for button in buttons])
    print(goal)
    visited = {0}
    while q:
        print(visited)
        button, state, numPresses = q.popleft()
        print(button, state)
        if state == 10 and button == 12:
            print("gooooo")
        if state == goal:
            print("hiiiiii")
            return numPresses
        state = applyButton(button, state)
        for button in buttons:
            if state not in visited:
                q.append((button, state, numPresses + 1))
                visited.add(state)

def part1(input):
    print("Part 1: ")
    sum = 0
    for line in input:
        goal, buttons, _ = line
        goal = parseGoal(goal)
        buttons = parseButtons(buttons)
        sum += bfs(goal, buttons)
    print(sum)

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
input = parseInput(filename)

part1(input)
part2(input)