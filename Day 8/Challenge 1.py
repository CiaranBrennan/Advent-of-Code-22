input = open('Day 8\\input.txt', 'r')
grid = []

for line in input:
    grid.append([int(digit) for digit in line.strip()])
noOfTrees = (len(grid) + len(grid[0])) * 2 - 4

for col in range(1, len(grid[0]) - 1):
    for row in range(1, len(grid) - 1):
        current = grid[row][col]
        lView = max(grid[row][:col])
        rView = max(grid[row][col+1:])
        uView = dView = 0
        for i in range(0, len(grid)):
            if i < row:
                uView = max(uView, grid[i][col])
            elif i > row:
                dView = max(dView, grid[i][col])
    
        if current > min(lView, rView, uView, dView):
            noOfTrees += 1
print(noOfTrees)