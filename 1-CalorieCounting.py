# Advent of Code Day 1
# 12/1/2022
#
#Problem 1
# Goal: Find the Elf carrying the most Calories.
#       How many total Calories is that Elf carrying?
#
#Problem 2
#Goal: Find the top three Elves carrying the most Calories.
#       How many Calories are Elves carrying in total?

def readFile():
    fileInput = open("input.txt")
    fileData = fileInput.read()
    fileInput.close()
    return fileData

def cleanData(data):
    data = data.split("\n\n")
    for i in range(len(data)):
        data[i] = data[i].split()
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    return data

def findMax(elfList):
    maxCalories = 0
    for i in elfList:
        if sum(i) > maxCalories:
            maxCalories = sum(i)
    return maxCalories

def findMaxThree(elfList):
    elfList.sort(key=sum)
    maxThree = 0
    for i in elfList[-3:]:
        maxThree += sum(i)
    return maxThree

def main():
    elfList = cleanData(readFile())
    maxCalories = findMax(elfList)
    highestThree = findMaxThree(elfList)
    print("Solution 1: Total -",maxCalories)
    print("Solution 2: Total -",highestThree)
 
main()
    
