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
        [warehouse, moves] = f.read().split('\n\n')
        warehouse = [[c for c in line] for line in warehouse.rstrip().split('\n')]
        moves = moves.rstrip().replace("\n", "")
        return warehouse, moves

def findRobot(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '@':
                return (i, j)
        
def mapMove(move, i, j):
    match move:
        case '<':
            return i, j - 1
        case '^':
            return i - 1, j
        case '>':
            return i, j + 1
        case 'v':
            return i + 1, j

def applyMove(warehouse, i, j, move):
    y, x = mapMove(move, i, j)
    if warehouse[y][x] == '#':
        return False, i, j
    if warehouse[y][x] == '.':
        warehouse[y][x] = warehouse[i][j]
        warehouse[i][j] = '.'
        return True, y, x
    if warehouse[y][x] == 'O':
        result, _, _ = applyMove(warehouse, y, x, move)
        if result:
            warehouse[y][x] = warehouse[i][j]
            warehouse[i][j] = '.'
            return result, y, x
        return result, i, j
    
def score(warehouse):
    score = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == 'O':
                score += 100 * i + j
    return score

def part1(warehouse, moves):
    print("Part 1: ")
    # prettyPrintLines(warehouse)
    # print(moves)
    (i, j) = findRobot(warehouse)
    for move in moves:
        _, i, j = applyMove(warehouse, i, j, move)
    # prettyPrintMatrix(warehouse)
    print(score(warehouse))

def transformMap(warehouse):
    output = []
    for row in warehouse:
        line = []
        for c in row:
            match c:
                case '#':
                    line.extend(['#', '#'])
                case 'O':
                    line.extend(['[', ']'])
                case '.':
                    line.extend(['.', '.'])
                case '@':
                    line.extend(['@', '.'])
        output.append(line)
    return output

def canMove(warehouse, i, j, move, moveQueue):
    (y, x) = mapMove(move, i, j)
    if warehouse[y][x] == '#':
        return False
    if warehouse[y][x] == '.':
        moveQueue[(y, x)] = warehouse[i][j]
        return True
    if warehouse[y][x] == '[':
        match move:
            case '<':
                result = canMove(warehouse, y, x, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                return result
            case '>':
                result = canMove(warehouse, y, x, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                return result
            case '^':
                result = canMove(warehouse, y, x, move, moveQueue) and canMove(warehouse, y, x + 1, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                    if (y, x + 1) not in moveQueue:
                        moveQueue[(y, x + 1)] = '.'
                return result
            case 'v':
                result = canMove(warehouse, y, x, move, moveQueue) and canMove(warehouse, y, x + 1, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                    if (y, x + 1) not in moveQueue:
                        moveQueue[(y, x + 1)] = '.'
                return result
    if warehouse[y][x] == ']':
        match move:
            case '<':
                result = canMove(warehouse, y, x, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                return result
            case '>':
                result = canMove(warehouse, y, x, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                return result
            case '^':
                result = canMove(warehouse, y, x, move, moveQueue) and canMove(warehouse, y, x - 1, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                    if (y, x - 1) not in moveQueue:
                        moveQueue[(y, x - 1)] = '.'
                return result
            case 'v':
                result = canMove(warehouse, y, x, move, moveQueue) and canMove(warehouse, y, x - 1, move, moveQueue)
                if result:
                    moveQueue[(y, x)] = warehouse[i][j]
                    if (y, x - 1) not in moveQueue:
                        moveQueue[(y, x - 1)] = '.'
                return result

def score2(warehouse):
    score = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '[':
                score += 100 * i + j
    return score

def part2(warehouse, moves):
    print("\nPart 2: ")
    warehouse = transformMap(warehouse)
    # prettyPrintMatrix(warehouse)
    (i, j) = findRobot(warehouse)
    for moveNum, move in enumerate(moves):
        moveQueue = {}
        result = canMove(warehouse, i, j, move, moveQueue)
        if result:
            for (y, x), c in moveQueue.items():
                warehouse[y][x] = c
            warehouse[i][j] = '.'
            (i, j) = mapMove(move, i, j)
        # print("move Number {}: {}".format(moveNum, move))
        # prettyPrintMatrix(warehouse)
    # prettyPrintMatrix(warehouse)
    print(score2(warehouse))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
warehouse, moves = parseInput(filename)

part1(copy.deepcopy(warehouse), moves)
part2(warehouse, moves)