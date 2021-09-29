import sys
import math
import string
# Practice Scenario:https://wma.contest.lmcodequestacademy.com/team/problems/9/text

testCases = int(input())
asteroidArray1 = []
asteroidArray2 = []

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
    if (currentCase==0):
        for i in range(numAsteroids):
            asteroid = input()
            str(asteroid)
            asteroidArray1.append(asteroid)
            i = i+1
    if (currentCase==1):
        for i in range(numAsteroids):
            asteroid = input()
            str(asteroid)
            asteroidArray2.append(asteroid)
            i = i+1
    z = z+1


for i in range((len(asteroidArray1))-1):
    for i in range((len(asteroidArray1))-1):
        if ((distanceCalc(asteroidArray1[i])) > (distanceCalc(asteroidArray1[i+1]))):
            temp1 = asteroidArray1[i]
            temp2 = asteroidArray1[i+1]
            asteroidArray1[i] = temp2
            asteroidArray1[i+1] = temp1
        i = i+1

for i in range((len(asteroidArray2))-1):
    for i in range((len(asteroidArray2))-1):
        if ((distanceCalc(asteroidArray2[i])) > (distanceCalc(asteroidArray2[i+1]))):
            temp1 = asteroidArray2[i]
            temp2 = asteroidArray2[i+1]
            asteroidArray2[i] = temp2
            asteroidArray2[i+1] = temp1
        i = i+1

print("----------")
for i in range(len(asteroidArray1)):
    print(asteroidArray1[i])
    i = i+1
for i in range(len(asteroidArray2)):
    print(asteroidArray2[i])
    i = i+1

