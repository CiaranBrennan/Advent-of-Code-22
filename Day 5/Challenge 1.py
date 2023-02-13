input = open('Day 5\\input.txt', 'r').readlines()

stacks = []

buildingStack = True
firstRow = True
index = -1

for row in input:
    index += 1
    if buildingStack:
        if row[1] != '1':
            noOfStacks = 0
            for stackNo in range (1, len(row), 4):
                if firstRow:
                    if row[stackNo].isspace():
                        stacks.append([])
                    else:
                        stacks.append([row[stackNo]])
                else:
                    if not row[stackNo].isspace():
                        stacks[noOfStacks].append(row[stackNo])
                    noOfStacks += 1
            firstRow = False
        else:
            for i in range(0, noOfStacks):
                stacks[i] = stacks[i][::-1]
            break

for i in range(index + 2, len(input)):
    row = input[i].split(' ')
    numberOfTimes = int(row[1])
    moveFrom = int(row[3]) - 1
    moveTo = int(row[5]) - 1
    for j in range(0, numberOfTimes):
        try:
            stacks[moveTo].append(stacks[moveFrom].pop())
        except:
            print(stacks[moveFrom])

for stack in stacks:
    print(stack[-1])