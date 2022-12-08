import heapq

elfCalories = []

with open('input.txt') as f:
    lines = f.readlines()

Sum = 0
for line in lines:
    #print(line)
    calories = line.rstrip()
    if not calories:
        elfCalories.append(Sum)
        Sum = 0
    else:
        Sum += int(calories)

print(sum(heapq.nlargest(3, elfCalories)))