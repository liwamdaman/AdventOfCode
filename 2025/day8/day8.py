from math import sqrt, prod
import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
from typing import Counter
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def calculateDistance(point1, point2):
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)

### use Union-find data structure + algo to manage and combine disjoint sets ###
def makeSet(nodes):
    parents = {}
    for x in nodes:
        parents[x] = x
    return parents
def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])  # Path compression - flatten the tree
    return parents[x]
def union(parents, x, y):
    root_x, root_y = find(parents, x), find(parents, y)
    if root_x != root_y:
        parents[root_x] = root_y  # Point one root to the other

def part1(input, k):
    print("Part 1: ")
    maxHeap = []
    points = [Point(*map(int, line.split(","))) for line in input]
    for point1, point2 in itertools.combinations(points, 2):
        distance = -1 * calculateDistance(point1, point2)
        heapq.heappush(maxHeap, (distance, point1, point2))
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    closestPairs = []
    while maxHeap:
        top = heapq.heappop(maxHeap)
        closestPairs.append(top)
    closestPairs.reverse()
    parents = makeSet(points)
    for _, point1, point2 in closestPairs:
        union(parents, point1, point2)
    clusterSizes = Counter(find(parents, x) for x in points)
    top3 = sorted(clusterSizes.values(), reverse=True)[:3]
    res = prod(top3)
    print(res)

def part2(input):
    print("\nPart 2: ")
    minHeap = []
    points = [Point(*map(int, line.split(","))) for line in input]
    for point1, point2 in itertools.combinations(points, 2):
        distance = calculateDistance(point1, point2)
        heapq.heappush(minHeap, (distance, point1, point2))
    parents = makeSet(points)
    while True:
        closestPair = heapq.heappop(minHeap)
        _, point1, point2 = closestPair
        union(parents, point1, point2)   
        clusterSizes = Counter(find(parents, x) for x in points)
        if len(clusterSizes) == 1:
            print(point1.x * point2.x)
            break

dirname = os.path.dirname(__file__)
testSetup = ('test.txt', 10)
inputSetup = ('input.txt', 1000)
# Change this to switch between test and input 
chosenSetup = inputSetup
# chosenSetup = testSetup
filename = os.path.join(dirname, chosenSetup[0])
input = parseInput(filename)

part1(input, chosenSetup[1])
part2(input)