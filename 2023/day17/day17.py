import sys
import os
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *
import heapq
import time
import copy

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def generateNeighbours(node, city, shortestPathCosts, shortestPaths, isPart2, debug):
    # print(node)
    (cost, i, j, direction, streak) = node
    neighbours = []
    for (k,l,dir) in [(i-1,j,0), (i+1,j,1), (i,j-1,2), (i,j+1,3)]:
        strk = streak + 1 if dir == direction else 1
        # cannot reverse direction, and needs to maintain streak rules
        if not isDirectionValid(dir, direction, strk, streak, isPart2) or (direction == 0 and dir == 1) or (direction == 1 and dir == 0) or (direction == 2 and dir == 3) or (direction == 3 and dir == 2):
            continue
        if 0 <= k < len(city) and 0 <= l < len(city[0]):
            updatedCost = cost+int(city[k][l])
            if shortestPathCosts.get((k,l,dir,strk), (sys.maxsize)) <= updatedCost:
                continue
            shortestPathCosts[(k,l,dir,strk)] = updatedCost
            neighbour = (updatedCost,k,l,dir,strk)
            if debug:
                shortestPaths[neighbour] = copy.deepcopy(shortestPaths[node])
                shortestPaths[neighbour].append(node)
            neighbours.append(neighbour)
    return neighbours

def isDirectionValid(dir, direction, strk, streak, isPart2):
    if isPart2:
        return strk <= 10 and (streak >= 4 or dir == direction)
    return strk <= 3
    
def run(input, isPart2=False, debug=False):
    # I think this is Dijkstra’s Algorithm?? idk I didn't actually study it properly, just tried to figure it out
    city = parseLinesToMatrix(input)
    heap = []
    shortestPathCosts = {}

    # Just used for debugging
    shortestPaths = {}
    shortestPaths[(0, 0, 0, 3, 0)] = []
    shortestPaths[(0, 0, 0, 1, 0)] = []

    # We will model vertices as tuples, (cost, i, j, direction, streak)
    heapq.heappush(heap, (0, 0, 0, 3, 0))
    heapq.heappush(heap, (0, 0, 0, 1, 0))
    while heap:
        curr = heapq.heappop(heap)
        # print(curr)
        if curr[1] == len(city)-1 and curr[2] == len(city[0])-1 and not (isPart2 and curr[4] < 4):
            print(curr[0])
            # Only for debugging path
            if debug:
                print(shortestPaths[curr])
            return
        for neighbour in generateNeighbours(curr, city, shortestPathCosts, shortestPaths, isPart2, debug):
            heapq.heappush(heap, neighbour)

def part1(input):
    print("Part 1: ")
    run(input)
            

def part2(input):
    print("\nPart 2: ")
    run(input, True, False)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)