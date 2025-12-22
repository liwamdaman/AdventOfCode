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
from pulp import *
sys.setrecursionlimit(10000)
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
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

def part1(input):
    print("Part 1: ")

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
        initial = [(applyButton(button, 0), 1) for button in buttons]
        q = collections.deque(initial)
        visited = set(initial)
        while q:
            state, numPresses = q.popleft()
            if state == goal:
                return numPresses
            for button in buttons:
                newState = applyButton(button, state)
                if newState not in visited:
                    q.append((newState, numPresses + 1))
                    visited.add(newState)
    
    sum = 0
    for line in input:
        goal, buttons, _ = line
        goal = parseGoal(goal)
        buttons = parseButtons(buttons)
        sum += bfs(goal, buttons)
    print(sum)

def part2(input):
    print("\nPart 2: ")

    def parseButtons(buttons):
        return [[int(d) for d in button[1:-1].split(',')] for button in buttons]

    # Represent joltages as goal vector
    def parseJoltages(joltages):
        return [int(joltage) for joltage in joltages[1:-1].split(',')]

    def vectorizeButtons(buttons, joltages):
        N = len(joltages)
        res = []
        for button in buttons:
            vector = [0] * N
            for light in button:
                vector[light] = 1
            res.append(vector)
        return res

    ## Part two can be solved efficiently as a linear algebra problem, with integers only (ILP)
    res = 0
    for line in input:
        _, buttons, joltages = line
        buttons = parseButtons(buttons)
        joltages = parseJoltages(joltages)
        buttons = vectorizeButtons(buttons, joltages)
        buttons = getRotated90CWLines(buttons)

        #Using PulP
        prob = LpProblem("Minimize_ILP", LpMinimize)
        n_vars = len(buttons[0])
        x = [LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(n_vars)]
        prob += lpSum(x)
        equations = zip(buttons, joltages)
        for equation in equations:
            prob += lpSum(equation[0][i] * x[i] for i in range(n_vars)) == equation[1]
        # print(prob.constraints)
        prob.solve(PULP_CBC_CMD(msg=0))
        solution = [value(xi) for xi in x]
        # print(solution)
        res += int(sum(solution))

    print(res)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)