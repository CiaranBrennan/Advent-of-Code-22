assignments = open('Day 4\\input.txt', 'r').readlines()

numberOfOverlaps = 0
for assignment in range(0, len(assignments)):
    assignmentRange1 = assignments[assignment].split(',')[0]
    assignmentRange2 = assignments[assignment].split(',')[1]
    range1           = range(int(assignmentRange1.split('-')[0]), int(assignmentRange1.split('-')[1]))
    range2           = range(int(assignmentRange2.split('-')[0]), int(assignmentRange2.split('-')[1]))

    if (range1.start <= range2.start and range1.stop >= range2.start) or (range2.start <= range1.start and range2.stop >= range1.start):
        numberOfOverlaps += 1


print('Number of overlaps: ', numberOfOverlaps)
    