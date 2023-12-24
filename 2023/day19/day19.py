import sys
import os
import re
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]
    
class Flow():
    def __init__(self, name, conditions, final):
        self.name = name
        self.conditions = conditions
        self.final = final
    
    def addCondition(self, conditionString):
        self.conditions.append(re.search("(\w)(<|>)(\d+):(\w+)", conditionString).groups())

mapCategoryToDigit = {
    'x':0,
    'm':1,
    'a':2,
    's':3
}

def process(part, flow):
    for condition in flow.conditions:
        if processCondition(part, condition):
            return condition[3]
    return flow.final

def processCondition(part, condition):
    if condition[1] == '<':
        return part[mapCategoryToDigit[condition[0]]] < int(condition[2])
    return part[mapCategoryToDigit[condition[0]]] > int(condition[2])

def parseFlowsAndParts(lines):
    flowsList = []
    lineIter = iter(lines)
    for line in lineIter:
        if not line:
            break
        flowsList.append(line)
    partsList = []
    for line in lineIter:
        partsList.append(line)
    flows = {}
    for flow in flowsList:
        flowName = flow.split('{')[0]
        conditions = re.findall("(\w+[<|>]\d+:\w+),", flow)
        final = flow.split(',')[-1].split('}')[0]
        flows[flowName] = Flow(flowName, [], final)
        for condition in conditions:
            flows[flowName].addCondition(condition)
    parts = [tuple(map(int, re.search(".*=(\d+),.*=(\d+),.*=(\d+),.*=(\d+)", part).groups())) for part in partsList]
    return flows, parts

def part1(input):
    print("Part 1: ")
    flows, parts = parseFlowsAndParts(input)
    Sum = 0
    for part in parts:
        flow = flows['in']
        while (result := process(part, flow)) not in 'AR':
            flow = flows[result]
        # print(result)
        if result == 'A':
            Sum += sum(part)
    print(Sum)

def part2(input):
    print("\nPart 2: ")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input = parseInput(filename)

timeFunction(part1, input)
part2(input)