with open('input.txt') as f:
    lines = f.readlines()

numOverlap=0

for line in lines:
    first, second = line.split(',')
    firstStart, firstEnd = map(int, first.split('-'))
    secondStart, secondEnd = map(int, second.split('-'))
    if firstStart <= secondStart and firstEnd >= secondEnd:
        numOverlap += 1
    elif secondStart <= firstStart and secondEnd >= firstEnd:
        numOverlap += 1

print(numOverlap)
