rucksacks = open("Day 3\\input.txt", "r")

compartments = ['','']
totalPriority = 0
for rucksack in rucksacks:
    itemFound = 0
    compartments[0], compartments[1] = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

    for item1 in compartments[0]:
        if itemFound:
            break

        for item2 in compartments[1]:
            if item1 == item2:
                print(item1, ' is equal to ', item2)
                totalPriority += ord(item1.lower()) - 96
                if item1.isupper():
                    totalPriority += 26
                itemFound = 1
                break
                
print("Total priority is: ", totalPriority)
