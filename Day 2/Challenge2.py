guide = open("Day 2\\input.txt", "r")

scores = {
    "X": 0,
    "Y": 3,
    "Z": 6,
    "A": 0,
    "B": 1,
    "C": 2
}

totalScore = 0
for round in guide:
    totalScore += scores[round[2]]
    if round[2] == "X":
        totalScore += (scores[round[0]] - 1) %3 + 1
    elif round[2] == "Z":
        totalScore += (scores[round[0]] + 1) %3 + 1
    else:
        totalScore += scores[round[0]] + 1

print(totalScore)