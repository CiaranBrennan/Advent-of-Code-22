guide = open("Day 2\input.txt", "r")

scores = {
    "X": 0,
    "Y": 1,
    "Z": 2,
    "A": 0,
    "B": 1,
    "C": 2
}

totalScore = 0
for round in guide:
    totalScore += scores[round[2]] + 1
    if scores[round[2]] == (scores[round[0]] + 1) %3:
        totalScore += 6
    elif scores[round[2]] == scores[round[0]]:
        totalScore += 3

print(totalScore)