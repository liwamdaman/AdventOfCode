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
        machines = f.read().split('\n\n')
        result = []
        for machine in machines:
            [buttonA, buttonB, prize] = machine.rstrip().split('\n')
            result.append([[int(x) for x in re.findall(r"\+(\d+)", buttonA)], [int(x) for x in re.findall(r"\+(\d+)", buttonB)], [int(x) for x in re.findall(r"=(\d+)", prize)]])
        # print(result)
        return result

def cramersRule(machine):
    D = machine[0][0] * machine[1][1] - machine[0][1] * machine[1][0]
    Da = machine[2][0] * machine[1][1] - machine[2][1] * machine[1][0]
    Db = machine[0][0] * machine[2][1] - machine[0][1] * machine[2][0]
    if D == 0:
        print("uh oh")
        return 0, 0
    A = Da/D
    B = Db/D
    if int(A) == A and int(B) == B:
        return A, B
    return 0, 0

def part1(input):
    print("Part 1: ")
    sum = 0
    for machine in input:
        A, B = cramersRule(machine)
        # print(A)
        # print(B)
        cost = A * 3 + B * 1
        sum += cost
    print(sum)

def part2(input):
    print("\nPart 2: ")
    sum = 0
    for machine in input:
        machine[2][0] += 10000000000000
        machine[2][1] += 10000000000000
        A, B = cramersRule(machine)
        cost = A * 3 + B * 1
        sum += cost
    print(sum)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)