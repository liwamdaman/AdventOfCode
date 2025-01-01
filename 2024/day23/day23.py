import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
import networkx as nx
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def part1(input):
    print("Part 1: ")
    G = nx.Graph()
    for line in input:
        [l, r] = line.split('-')
        G.add_edge(l, r)
    cliques = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3 and any(node.startswith('t') for node in clique)]
    print(len(cliques))

def part2(input):
    print("\nPart 2: ")
    G = nx.Graph()
    for line in input:
        [l, r] = line.split('-')
        G.add_edge(l, r)
    lanParty = max(nx.find_cliques(G), key=len)
    print(",".join(sorted(lanParty)))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

part1(input)
part2(input)