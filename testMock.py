import random


def doChoice(arr):
    return random.randint(0, len(arr) - 1)


def getHostChoiceArr(pArr, pChoiceIndex):
    hArr = []
    hIndex = 0
    for i in range(len(pArr) - 1):
        hArr.append(-1)
    for i in range(len(pArr)):
        if i == pChoiceIndex:
            continue
        else:
            hArr[hIndex] = pArr[i]
            hIndex += 1
    return hArr


def doMock():
    # player do choice
    pArr = [1, 0, 0, 0]
    pChoice = doChoice(pArr)

    # host do choice
    hArr = getHostChoiceArr(pArr, pChoice)
    hChoice = doChoice(hArr)

    if hArr[hChoice] == 0:  # host chooses wrong direction
        if pArr[pChoice] == 1:  # player chooses right direction
            return 1
        return 0  # player chooses wrong direction
    return -1  # invalidate condition


def test(n):
    playerWinC = 0
    playerFailC = 0
    inValidateC = 0
    for i in range(n):
        result = doMock()
        if result == 1:
            playerWinC += 1
        if result == 0:
            playerFailC += 1
        if result == -1:
            inValidateC += 1

    print "all samples:", n
    print "validate condition:", (playerFailC + playerWinC)
    print "invalidate condition:", inValidateC
    print "player wins count", playerWinC
    print "player fails count:", playerFailC
    print "player wins rate within validate condition ", "%.9f" % ((playerWinC * 1.0) / (playerWinC + playerFailC))
    print "player wins rate within whole samples", ((playerWinC * 1.0) / n)


test(1000000)
