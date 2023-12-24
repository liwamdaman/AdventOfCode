import sys
import os
import functools 
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def getNextVertex(curr, dir, n):
    match dir:
        case 'R':
            return (curr[0]+n, curr[1])
        case 'L':
            return (curr[0]-n, curr[1])
        case 'U':
            return (curr[0], curr[1]-n)
        case 'D':
            return (curr[0], curr[1]+n)
        
def determinant(p1, p2):
    return (p1[0])*(p2[1]) - (p1[1])*(p2[0])

def part1(input):
    print("Part 1: ")
    vertices = [(0,0)]
    b = 0
    for line in input:
        [dir, n, color] = line.split()
        n = int(n)
        b += n
        vertices.append(getNextVertex(vertices[-1], dir, n))
    # Shoelace formula
    area = 0
    for i, point in enumerate(vertices):
        if i == 0: continue
        area += determinant(vertices[i-1], point)/2
    # Pick's theorem: A = I + B/2 – 1, isolating for I
    i = area - (b/2) + 1
    print(int(b + i))

digitToDir = {'0':'R','1':'D','2':'L','3':'U'}

def part2(input):
    print("\nPart 2: ")
    vertices = [(0,0)]
    b = 0
    for line in input:
        color = line.split()[2]
        n = int(color[2:7],16)
        b += n
        dir = digitToDir[color[7]]
        vertices.append(getNextVertex(vertices[-1], dir, n))
    # Shoelace formula
    area = 0
    for i, point in enumerate(vertices):
        if i == 0: continue
        area += determinant(vertices[i-1], point)
    area /= 2
    # Pick's theorem: A = I + B/2 – 1, isolating for I
    i = area - (b/2) + 1
    print(int(b + i))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)
