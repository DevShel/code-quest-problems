import sys
import math
import string
# Practice Scenario:https://wma.contest.lmcodequestacademy.com/team/problems/8/text

testCases = int(input())
inputArray = []

for i in range(testCases):
    inputText = input()
    str(inputText)
    inputArray.append(inputText)

for i in range(testCases):
    tempCase = inputArray[i]
    if (tempCase[14]=="E"): #this is input for parentheses
        print("(" + tempCase[0:3] + ") " + tempCase[3:6] + "-" + tempCase[6:10])
    if (tempCase[14]=="H"): #this is input for dashes
        print(tempCase[0:3] + "-" + tempCase[3:6] + "-" + tempCase[6:10])
    if (tempCase[14]=="I"): #this is input for periods
        print(tempCase[0:3] + "." + tempCase[3:6] + "." + tempCase[6:10])
    i = i+1
 



