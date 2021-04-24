import sys
import math
import string
# Practice Scenario:https://wma.contest.lmcodequestacademy.com/team/problems/8/text

def phone_book_output(inputText):
    str(inputText)
    if (inputText[14]=="E"): #this is input for parentheses
        print("(" + inputText[0:3] + ") " + inputText[3:6] + "-" + inputText[6:10])
    if (inputText[14]=="H"): #this is input for dashes
        print(inputText[0:3] + "-" + inputText[3:6] + "-" + inputText[6:10])
    if (inputText[14]=="I"): #this is input for periods
        print(inputText[0:3] + "." + inputText[3:6] + "." + inputText[6:10])

inputText = input()
phone_book_output(inputText)


