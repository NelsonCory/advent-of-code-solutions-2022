#Advent of  Code Day 2
#12/2/2022
#
#
# Problem 1:
#   Goal: What would your total score be if everything
#       goes exactly according to the strategy guide?
#
# Problem 2:
#   Goal: What would your total score be if everything goes
#       according to the strategy guide? (different strategy)
#

#part 1 maps
decodeMap = {"X":"A","Y":"B","Z":"C"}
choiceMap = {"A":"rock","B":"paper","C":"scissors"}
pointsMap = {"draw":3,"win":6,"lose":0,"rock":1,"paper":2,"scissors":3}

#part 2 decodemap
decodeMap2 = {"X":2,"Y":1,"Z":0} #lose, draw, win
choiceMap2 = {"A":["B","A","C"],"B":["C","B","A"],"C":["A","C","B"]}

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
def didPlayerWin(playerChoice,aiChoice): #part 1
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
    
    #part 1
    score = 0
    for i in data:
        playerChoice = choiceMap.get(decodeMap.get(i[1]))
        aiChoice = choiceMap.get(i[0])
        score += pointsMap.get(playerChoice)
        score += pointsMap.get(didPlayerWin(playerChoice,aiChoice))
    print("Part 1:",score)

    #part 2
    score = 0
    for i in data:
        playerChoice = choiceMap.get(choiceMap2.get(i[0])[decodeMap2.get(i[1])])
        aiChoice = choiceMap.get(i[0])
        goal = decodeMap2.get(i[1])
        score += pointsMap.get(playerChoice)
        score += pointsMap.get(didPlayerWin(playerChoice,aiChoice))
        #print(aiChoice,playerChoice,goal)
    print("Part 2:",score)


   
main(); 

