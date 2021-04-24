import sys
import math
import string
# Practice Scenario:https://wma.contest.lmcodequestacademy.com/team/problems/9/text

testCases = int(input())
asteroidArray = []

def distanceCalc(coordinates):
    if coordinates[0] == "-":
        x = int(coordinates[1])
        y = int(coordinates[3])
    elif coordinates[2] == "-":
        x = int(coordinates[0])
        y = int(coordinates[3])
    else:
        x = int(coordinates[0])
        y = int(coordinates[2])

    distance = math.sqrt((x^2)+(y^2))
    return(distance)


for z in range(testCases):
    currentCase = z
    numAsteroids = int(input())
    for i in range(numAsteroids):
        asteroid = input()
        str(asteroid)
        asteroidArray.insert(currentCase,asteroid)
        i = i+1
    z = i+1


for i in range((len(asteroidArray))-1):
    for i in range((len(asteroidArray))-1):
        if ((distanceCalc(asteroidArray[i])) > (distanceCalc(asteroidArray[i+1]))):
            temp1 = asteroidArray[i]
            temp2 = asteroidArray[i+1]
            asteroidArray[i] = temp2
            asteroidArray[i+1] = temp1
        i = i+1

for i in range(testCases):
    for x in range(testCases):
        print (asteroidArray[i][x])
        x = x+1
    i = i+1
    


