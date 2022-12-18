#Advent of  Code Day 2
#12/2/2022
#
#
# Problem 1:
#   Goal: What would your total score be if everything
#       goes exactly according to the strategy guide?
#

decodeMap = {"X":"A","Y":"B","Z":"C"}
choiceMap = {"A":"rock","B":"paper","C":"scissors"}
pointsMap = {"draw":3,"win":6,"lose":0,"rock":1,"paper":2,"scissors":3}


def readFile():
    fileInput = open("input.txt")
    fileData = fileInput.read()
    fileInput.close()
    return fileData

def cleanInput(fileInput):
    #input consists of pairs of (ABC):(XYZ)
    fileInput = fileInput.split("\n")
    for i in range(len(fileInput)):
        fileInput[i] = fileInput[i].split(" ")
    
    return fileInput

    
#rock = 1, paper = 2. scissors = 3
# 0 loss, 3 draw, 6 win

def didPlayerWin(playerChoice,aiChoice):
    if playerChoice == aiChoice:
        return "draw"
    elif playerChoice == "rock" and aiChoice == "scissors":
        return "win"
    elif playerChoice == "scissors" and aiChoice == "paper":
        return "win"
    elif playerChoice == "paper" and aiChoice == "rock":
        return "win"
    else:
        return "lose"

def main():
    data = cleanInput(readFile())
    score = 0
    for i in data:
        playerChoice = choiceMap.get(decodeMap.get(i[1]))
        aiChoice = choiceMap.get(i[0])
        score += pointsMap.get(playerChoice)
        score += pointsMap.get(didPlayerWin(playerChoice,aiChoice))
    
    print(score)
    
main(); 

