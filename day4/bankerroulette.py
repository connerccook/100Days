import random
names = input(
    "What are your names? Please seperate each name with comma and space: ")

nameList = names.split(", ")
randNum = random.randint(0, len(nameList))

print(nameList[randNum])
