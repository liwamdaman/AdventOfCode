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
        return [line.rstrip() for line in lines]

def calculateArea(point1, point2):
    return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

def part1(input):
    print("Part 1: ")
    maxArea = 0
    points = [(int(x), int(y)) for x, y in [line.split(",") for line in input]]
    for pair in itertools.combinations(points, 2):
        area = calculateArea(pair[0], pair[1])
        maxArea = max(maxArea, area)
    print(maxArea)

# # initial approach: add fake/intermediate vertices at possible break points on edge of polygon
# # EDIT: nah this doesn't work
# def part2(input):
#     print("\nPart 2: ")
#     points = [(int(x), int(y)) for x, y in [line.split(",") for line in input]]
#     rows = set()
#     cols = set()
#     for point in points:
#         rows.add(point[0])
#         cols.add(point[1])
#     newPoints = points.copy()
#     # Trace outline of polygon, adding intermediate points
#     for i, point in enumerate(points[1:] + points[-1:]):
#         prevPoint = points[i]
#         if prevPoint[0] == point[0]:
#             increment = 1 if point[1] > prevPoint[1] else -1
#             for y in range(prevPoint[1] + increment, point[1], increment):
#                 if y in cols:
#                     newPoints.append((point[0], y))
#         else:
#             increment = 1 if point[0] > prevPoint[0] else -1
#             for x in range(prevPoint[0] + increment, point[0], increment):
#                 if x in rows:
#                     newPoints.append((x, point[1]))
#     # print(newPoints)
#     maxArea = 0
#     for pair in itertools.combinations(newPoints, 2):
#         area = calculateArea(pair[0], pair[1])
#         maxArea = max(maxArea, area)
#     print(maxArea)

# Ray casting algorithm to determine if a point is within the polygon
def isPointInPolygon(point, verticalEdges, outlineSet, compressedPoints, cache):
    if point in outlineSet:
        return True
    if point in cache:
        return cache[point]
    x, y = point
    # Cast ray to the right, count edge crossings
    crossings = 0
    for testX in range(x+1, max([p[0] for p in compressedPoints]) + 1):
        for yRange in verticalEdges[testX]:
            # This is kinda weird, but don't use <= on both sides, just one, for handling the edge case where the 
            # ray travels across a horizontal line and technically crosses two vertical edges, but it should only 
            # be considered as one crossing because one of the vertical edges is just above and one is just below.
            if yRange[0] <= y < yRange[1]:
                crossings += 1
                break
    res = crossings % 2 == 1
    cache[point] = res
    return res

# Next approach, using some advice: Apply coordinate compression to use less memory
# Then, for each point within a candidate rectangle, check if it is within the polygon using ray-casting algorithm.
def part2(input):
    print("\nPart 2: ")
    points = [(int(x), int(y)) for x, y in [line.split(",") for line in input]]
    # Apply coordinate compression, but crucially we need to maintain whitespace between edges
    xs = sorted(set(p[0] for p in points))
    ys = sorted(set(p[1] for p in points))
    Xs = []
    for x in xs:
        if Xs:
            Xs.append(-100)
        Xs.append(x)    
    Ys = []
    for y in ys:
        if Ys:
            Ys.append(-100)
        Ys.append(y)
    # print(Xs)
    # print(Ys)
    xMap = {x: i for i, x in enumerate(Xs)}
    yMap = {y: i for i, y in enumerate(Ys)}
    compressedPoints = [(xMap[p[0]], yMap[p[1]]) for p in points]

    # matrix = [['.'] * len(Xs) for _ in range(len(Ys))]
    # for x,y in compressedPoints:
    #     matrix[y][x] = 'x'
    # prettyPrintMatrix(matrix)

    # This is probably not the best way to do this, but we need some info for the ray casting algorithm.
    # Save set of all points on edges, and also a map of vertical edges (xVal -> [y1, y2])
    verticalEdges = collections.defaultdict(list)
    for i, point in enumerate(compressedPoints[1:] + compressedPoints[0:1]):
        prevPoint = compressedPoints[i]
        if prevPoint[0] == point[0]:
            verticalEdges[point[0]].append([min(prevPoint[1], point[1]), max(prevPoint[1], point[1])])
    outlineSet = set()
    for i, point in enumerate(compressedPoints[1:] + compressedPoints[0:1]):
        prevPoint = compressedPoints[i]
        if prevPoint[0] == point[0]:
            increment = 1 if point[1] > prevPoint[1] else -1
            for y in range(prevPoint[1], point[1], increment):
                outlineSet.add((prevPoint[0], y))
        else:
            increment = 1 if point[0] > prevPoint[0] else -1
            for x in range(prevPoint[0], point[0], increment):
                outlineSet.add((x, prevPoint[1]))

    # Generate candidate rectangles and check all points on perimeter of candidate rectangle
    maxArea = 0
    cache = {}
    for point1, point2 in itertools.combinations(compressedPoints, 2):
        valid = True
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            if (not isPointInPolygon((x, min(point1[1], point2[1])), verticalEdges, outlineSet, compressedPoints, cache) 
            or not isPointInPolygon((x, max(point1[1], point2[1])), verticalEdges, outlineSet, compressedPoints, cache)):
                valid = False
                break
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            if (not isPointInPolygon((min(point1[0], point2[0]), y), verticalEdges, outlineSet, compressedPoints, cache)
            or not isPointInPolygon((max(point1[0], point2[0]), y), verticalEdges, outlineSet, compressedPoints, cache)):
                valid = False
                break
        if valid:
            # map back to original coordinates and calculate area 
            point1Original = (Xs[point1[0]], Ys[point1[1]])
            point2Original = (Xs[point2[0]], Ys[point2[1]])
            maxArea = max(maxArea, calculateArea(point1Original, point2Original))
    print(maxArea)
                    
'''
Useful edge case test:
100,100
100,900
800,900
800,100
300,100
300,200
700,200
700,800
200,800
200,100

The correct answer should be
561501
80901
'''
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
# Runs in ~4.5 seconds on macbook pro
timeFunction(part2, input)