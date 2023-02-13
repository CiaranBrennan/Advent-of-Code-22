rucksacks = open("Day 3\\input.txt", "r").readlines()

totalPriority = 0

for rucksack in range(0, len(rucksacks), 3):
    for item in rucksacks[rucksack]:
        if item in rucksacks[rucksack + 1] and item in rucksacks[rucksack + 2]:
            totalPriority += ord(item.lower()) - 96
            if item.isupper():
                totalPriority += 26
            break

print("Total priority is: ", totalPriority)