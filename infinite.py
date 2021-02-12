numOfLoops = 0
numofApples = 2

while numOfLoops < 10:
    numofApples *= 2
    numofApples += numOfLoops
    numOfLoops -= 1
print('Number of Apples: ' + str(numofApples))
