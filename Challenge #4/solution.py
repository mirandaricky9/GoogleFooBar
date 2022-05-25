import copy

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

# prints the map to the terminal to be easily seen
def printMap(map):
    for i in map:
        print(i)
    # print(len(map)) # number of rows (height)
    # print(len(map[0])) # number of columns (width)


# map is a matrix that represents passable space (1s) and impassable walls (0s)
# the starting position is on the top left represented by the coordinate (0,0)
# the escape pod position is located at the bottom right (w-1, h-1)
# each coordinate (r, c) represents the row and the column of a space 
# we are allowed to remove one 'wall' in order to get to the escape pod

##### THOUGHTS: Conduct a simulation where you change only one of the walls and add that to a list of maps
# finds the shortest number of steps a bunny needs to take in order to get to the escape pod
def solution(map):
    # make a list of potential maps with only one wall removed for each spot there is a wall 
    # run solution on all of the maps
    maps = []
    print("DEBUGGING: I have made a list for maps")
    counts = []
    print("DEBUGGING: I have made a list for counts")
    maps.append(map)
    numMaps = 1
    for list in map:
        numMaps += list.count(1)

    # counts.append(generateCount(map))
    if(numMaps == 1):
        counts.append(len(map) + len(map[0]) - 1)
    print("DEBUGGING: I have generated a count for the default map")

    for i in range(len(map)): # for each row
        for j in range(len(map[0])): # for each column
            if (map[i][j] == 1):
                newMap = copy.deepcopy(map)
                map[i][j] = 0
                # print(f"The map is now:")
                # printMap(map)
                counts.append(generateCount(map))
                map[i][j] = 1
    print("DEBUGGING: I have generated counts for all possible maps")
    smallestCount = 999999
    for count in traverse(counts):
        if count < smallestCount and count != -1:
            smallestCount = count
    print("DEBUGGING: I have found the smallest count in the list of counts")
    return smallestCount


# finds the count for the current map 
# iterative and recursive approach 
def generateCount(map):        
    counts = [1] # the number of steps taken, including 
    tracker = ['0', '0'] # the current position of the bunny 

    # map[0][1] where 0 represents row 0 and 1 represents column 1 
    prevSteps = [] # a tracker of the previous steps (represented as a stack)

        # while the bunny has not reached the escape pod 
    while (tracker != [ str(len(map[0]) - 1), str(len(map) - 1) ]):
        
        row = int(tracker[0])
        column = int(tracker[1])

        # if we are not out of bounds regarding columns 
        if (column < len(map[0]) - 1):
            # if the step East is passable and it has not been passed yet
            if (map[row][column + 1] == 0 and prevSteps.count([str(row) ,str(column + 1)]) == 0):
               
                # if we are not out of bounds regarding rows
                if (row < len(map) - 1):
                    # if the step South is passable and it has not been passed yet
                    if (map[row + 1][column] == 0 and prevSteps.count([str(row + 1) , str(column)]) == 0):
                        # count += 1
                        # tracker[0] = str(row + 1)
                        # prevSteps.append([tracker[0], tracker[1]])
                        newMap = copy.deepcopy(map)
                        newMap[row][column + 1] = 1
                        counts.append(generateCount(newMap))
                    
                counts[0] += 1
                tracker[1] = str(column + 1)
                prevSteps.append([tracker[0], tracker[1]])
                continue
        if (row < len(map) - 1):
            if (map[row + 1][column] == 0 and prevSteps.count([str(row + 1) , str(column)]) == 0):
                counts[0] += 1
                tracker[0] = str(row + 1)
                prevSteps.append([tracker[0], tracker[1]])
                continue

        # checking to see if West or North are passable, respectively
        # and are not previous steps
        if (map[row][column - 1] == 0 and prevSteps.count([str(row) ,str(column - 1)]) == 0):
            counts[0] += 1
            tracker[1] = str(column - 1)
            prevSteps.append([tracker[0], tracker[1]])
            continue
        elif (map[row - 1][column] == 0 and prevSteps.count([str(row - 1) , str(column)]) == 0):
            counts[0] += 1
            tracker[0] = str(row - 1)
            prevSteps.append([tracker[0], tracker[1]])
            continue

        # if it has reached a dead end, break and make count equal -1 
        counts[0] = -1 
        break
        
    return counts




map1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
map2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
map3 = [[0,1,1],[0,0,1],[1,0,0]]
map4 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
map5 = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
map6 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

printMap(map4)
print(solution(map1))
print(solution(map2))
print(solution(map3))
print(solution(map4))

