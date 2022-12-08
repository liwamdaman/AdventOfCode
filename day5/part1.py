import re

# Hardcoding in initial stacks cuz I'm lazy and only have to do it once with this input
stacks = [
    ['R', 'S', 'L', 'F', 'Q'],
    ['N', 'Z', 'Q', 'G', 'P', 'T'],
    ['S', 'M', 'Q', 'B'],
    ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
    ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
    ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
    ['W', 'C', 'F'],
    ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
    ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
]

# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

with open('input.txt') as f:
    lines = f.readlines()

def parseLine(line):
    result = re.search("move (\d+) from (\d+) to (\d+)", line)
    # print(result.groups())
    return map(int, result.groups())

for line in lines:
    numMoves, src, dest = parseLine(line)
    # print(numMoves)
    # print(src)
    # print(dest)
    for i in range(numMoves):
        stacks[dest-1].append(stacks[src-1].pop())

# print output
ans = ""
for stack in stacks:
    ans += stack.pop()
print(ans)