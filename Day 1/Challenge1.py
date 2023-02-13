allFood = open("input.txt", "r")

maxCalories = 0
currentCalories = 0

for line in allFood:
    if line.isspace():
        if currentCalories > maxCalories:
            maxCalories = currentCalories
            print (maxCalories)
        currentCalories = 0
    else:
        currentCalories += int(line)
if currentCalories > maxCalories:
    maxCalories = currentCalories

print("The elf with the most calories has ", maxCalories, " calories of food")
