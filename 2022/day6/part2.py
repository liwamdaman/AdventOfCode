with open('input.txt') as f:
    line = f.readlines()[0]

for i in range(len(line)):
    last3 = set(line[i:i+14])
    if len(last3) == 14:
        print(i+14)
        break