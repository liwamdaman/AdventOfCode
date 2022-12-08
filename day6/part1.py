with open('input.txt') as f:
    line = f.readlines()[0]

for i in range(len(line)):
    last3 = set(line[i:i+4])
    if len(last3) == 4:
        print(i+4)
        break