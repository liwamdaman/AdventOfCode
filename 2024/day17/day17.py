import sys
import os
import collections
import copy
import functools
import re
import itertools
import heapq
sys.setrecursionlimit(10000)
sys.path.insert(1, '/Users/willi/adventOfCode/utils')
from utils import *

def parseInput(filename):
    with open(filename) as f:
        [registers, program] = f.read().split('\n\n')
        registers = registers.split('\n')
        A = int(registers[0].split(': ')[1])
        B = int(registers[1].split(': ')[1])
        C = int(registers[2].split(': ')[1])
        program = [int(x) for x in program.split(': ')[1].rstrip().split(',')]
        return A, B, C, program

class day17:
    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.programString = ','.join(str(x) for x in program)
        self.programPointer = 0
        self.output = ""

    def getCombo(self, operand):
        mapping = [
            0, 1, 2, 3, self.A, self.B, self.C
        ]
        return mapping[operand]

    def adv(self, operand):
        self.A = int(self.A / (2 ** self.getCombo(operand)))

    def bxl(self, operand):
        self.B = self.B ^ operand

    def bst(self, operand):
        self.B = self.getCombo(operand) % 8

    def jnz(self, operand):
        if self.A == 0:
            return
        self.programPointer = operand

    def bxc(self, operand):
        self.B = self.B ^ self.C

    def out(self, operand):
        if self.output != "":
            self.output += ','
        self.output += str(self.getCombo(operand) % 8)

    def bdv(self, operand):
        self.B = int(self.A / (2 ** self.getCombo(operand)))

    def cdv(self, operand):
        self.C = int(self.A / (2 ** self.getCombo(operand)))

    def mapInstruction(self, opcode):
        instructions = [
            self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv
        ]
        return instructions[opcode]

    def part1(self):
        # print('A: {}, B: {}, C: {}, program: {}'.format(self.A, self.B, self.C, self.program))
        prevPointer = 0
        while self.programPointer < len(self.program):
            # print(self.programPointer)
            self.mapInstruction(self.program[self.programPointer])(self.program[self.programPointer + 1])
            if self.programPointer == prevPointer:
                self.programPointer += 2
            prevPointer = self.programPointer

    # def part2(self):
    #     # Trying brute force
    #     i = 0
    #     while True:
    #         self.A = i
    #         self.B = 0
    #         self.C = 0
    #         self.programPointer = 0
    #         self.output = ""
    #         prevPointer = 0
    #         while self.programPointer < len(self.program):
    #             self.mapInstruction(self.program[self.programPointer])(self.program[self.programPointer + 1])
    #             if self.programPointer == prevPointer:
    #                 self.programPointer += 2
    #             prevPointer = self.programPointer
    #             # if self.programString[:len(self.output)] != self.output:
    #             #     break
    #         if self.programString == self.output:
    #             # program completed, output matches
    #             print(i)
    #             return
    #         print('A: {}, output: {}'.format(i, self.output))
    #         i += 1

    # originally didn't understand why this has to be recursive, and we couldn't just go digit by digit algorithmically. 
    # Its because for a given desired digit, there might be multiple i for i in range(8) that work, but will lead to a dead end later on. 
    def fuck(self, program, desiredIdx, currA):
        if desiredIdx < 0:
            print(currA >> 3)
            return True
        for i in range(8):
            A = currA + i
            B = A % 8
            B ^= 1
            C = A // (2 ** B)
            B ^= C
            B ^= 4
            out = B % 8
            if out == program[desiredIdx]:
                if self.fuck(program, desiredIdx - 1, (currA + i << 3)):
                    return True
        return False

    def part2(self):
        self.fuck(self.program, len(self.program) - 1, 0)

## TESTS ##
# test1 = day17(0, 0, 9, [2, 6])
# test1.part1()
# assert test1.B == 1

# test2 = day17(10, 0, 0, [5,0,5,1,5,4])
# test2.part1()
# assert test2.output == '0,1,2'

# test3 = day17(2024, 0, 0, [0,1,5,4,3,0])
# test3.part1()
# assert test3.output == '4,2,5,6,7,7,7,7,3,1,0'
# assert test3.A == 0

# test4 = day17(0, 29, 0, [1,7])
# test4.part1()
# assert test4.B == 26

# test5 = day17(0, 2024, 43690, [4,0])
# test5.part1()
# assert test5.B == 44354

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
A, B, C, program = parseInput(filename)

aoc = day17(A, B, C, program)
print("Part 1: ")
aoc.part1()
print(aoc.output)

aoc = day17(A, B, C, program)
print("\nPart 2: ")
aoc.part2()