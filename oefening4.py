import random

def countTargetPairs(lijst):
    target = input(int('geef een nummer als target voor het maken van paren'))
    aantalparen = 0
    for i in len(lijst) with 0 <= i and j in len(lijst) with 0 <= j:
        if  i < j and i + j < target :
            aantalparen = aantalparen + 1
    return aantalparen


list = []

while len(list) < 10:
    getal = random.randint
    if getal in range(-10, 10):
        list.append(getal)

antwoord = countTargetPairs(list)
print("het aantal paren zijn" + str(antwoord))