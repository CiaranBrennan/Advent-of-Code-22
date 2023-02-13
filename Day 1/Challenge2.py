allFood = open("input.txt", "r")

topThreeCalories = [0, 0, 0]
currentCalories = 0

for line in allFood:
    if line.isspace():
        for i in range(2, -1, -1):
            if currentCalories > topThreeCalories[i]:
                for j in range (0, i):
                    topThreeCalories[j] = topThreeCalories[j + 1]
                topThreeCalories[i] = currentCalories
                break
        currentCalories = 0
    else:
        currentCalories += int(line)
        
for i in range(2, -1, -1):
    if currentCalories > topThreeCalories[i]:
        for j in range (0, i):
            topThreeCalories[j] = topThreeCalories[j + 1]
        topThreeCalories[i] = currentCalories
        break
print(sum(topThreeCalories))