input = open('Day 7\\input.txt', 'r').readlines()
fileLength = len(input)
matchingDirectories = dict()

currentPath = '/root'
folderStructure = {'/root': 0}
totalSize = 0

for line in input:
    command = line.split()
    if command[0] == '$':
        if command[1] == 'ls':
            pass
        else:
            if command[2] == '..':
                currentPath = currentPath[:currentPath.rindex('/')]
            elif command[2] == '/':
                currentPath = '/root'
            else:
                currentPath = currentPath + '/' + command[2]
                folderStructure[currentPath] = 0
    else:
        if command[0] != 'dir':
            tempPath = currentPath
            while tempPath != '':
                folderStructure[tempPath] += int(command[0])
                tempPath = tempPath[:tempPath.rindex('/')]

for path, size in folderStructure.items():
    if size <= 100000:
        totalSize += size
        
print(totalSize)