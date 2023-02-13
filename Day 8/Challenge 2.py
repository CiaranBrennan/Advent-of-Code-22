input = open('Day 8\\input.txt', 'r')
grid = []
bestScore = 0
for line in input:
    grid.append([int(digit) for digit in line.strip()])

def viewCheck(position, view):
    lSight = rSight = 0
    for i in range(position - 1, -1, -1):
        if view[i] < view[position]:
            lSight += 1
        else:
            lSight += 1
            break

    for i in range(position + 1, len(view)):
            if view[i] < view[position]:
                rSight += 1
            else:
                rSight += 1
                break
    return lSight, rSight

for row in range(1, len(grid[0]) - 1):
    for col in range(1, len(grid) - 1):
        column = list(zip(*grid))[col]
        lView, rView = viewCheck(col, grid[row])
        uView, dView = viewCheck(row, column)
        score = lView * rView * uView * dView
        bestScore = max(score, bestScore)

print(bestScore)