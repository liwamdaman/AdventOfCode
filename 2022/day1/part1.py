elfCalories = []

with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    #print(line)
    calories = line.rstrip()
    if not calories:
        elfCalories.append(sum)
        sum = 0
    else:
        sum += int(calories)

# print(elfCalories)

print(max(elfCalories))