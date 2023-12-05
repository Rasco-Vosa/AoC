import os
import numpy as np
import matplotlib.pyplot as plt


#store Valid Numbers and corresponding label (each gear as a numeric label)
def getNumberAndLabel(MappedArray, contactPointsLabel, origElemArray):
    savedValidNumbers = []
    for i in range(0, np.shape(MappedArray)[0]):
        numb = ""
        validNumber = False

        for j in range(0, np.shape(MappedArray)[1]):
            if MappedArray[i,j] == 1:
                numb = numb + origElemArray[i,j]
                if (contactPointsLabel[i,j]>0): 
                    validNumber = True
                    idGear = contactPointsLabel[i,j]

                if j<np.shape(MappedArray)[1]-1:
                    if ((MappedArray[i,j+1] != 1)): 
                        if validNumber == True: savedValidNumbers.append([int(numb), idGear])
                        numb = ""
                        validNumber = False
                else:
                    if (validNumber == True): 
                        savedValidNumbers.append([int(numb), idGear])
                        numb = ""
                        validNumber = False
    return savedValidNumbers


# Check if "*"" can become gears and creates ContactPoints Matrix with label per gear
def CheckGears_ContactPoints(convArray):
    contactPointsLabel = np.zeros(np.shape(convArray)) # contact points label by gear they are in contact
    possibleGearsIdx = np.where(convArray == 2)
    gearID = 0
    for i in range(0, np.shape(possibleGearsIdx)[1]):
        NumberOfConnections = 0
        GearNeighbourMatrix = 1*(convArray[possibleGearsIdx[0][i]-1:possibleGearsIdx[0][i]+2, possibleGearsIdx[1][i]-1:possibleGearsIdx[1][i]+2] == 1)
        for k in range (0, len(GearNeighbourMatrix)):
            if np.array_equal(GearNeighbourMatrix[k,],np.array([1, 0, 1])): NumberOfConnections += 2
            elif np.array_equal(GearNeighbourMatrix[k,],np.array([0, 0, 0])): NumberOfConnections += 0
            else: NumberOfConnections += 1

        if NumberOfConnections == 2:
            gearID += 1
            contactPointsLabel[possibleGearsIdx[0][i]-1:possibleGearsIdx[0][i]+2, possibleGearsIdx[1][i]-1:possibleGearsIdx[1][i]+2] = GearNeighbourMatrix*gearID
        else: 
            convArray[possibleGearsIdx[0][i],possibleGearsIdx[1][i]] = 0
    
    return convArray, contactPointsLabel


def main (): 
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day3-input.txt')
    txtData = open(filePath,'r').read()
    
    # Convert array to matrix of 0,1,2 
    npArray = np.array([list(row) for row in txtData.split('\n')])
    convArray = np.select([npArray == '.', np.char.isdigit(npArray), npArray == '*'], [0, 1, 2], default=3)

    # Find Contact Points (already labeled) and update possible Gears to Valid Gears
    elementsMap, contactPointsLabel = CheckGears_ContactPoints(convArray)

    # Get Array with Number and a Label
    savedValidNumbers = getNumberAndLabel(elementsMap, contactPointsLabel, npArray)

    #Final math calculations
    indices = np.array(savedValidNumbers)[:,1]
    validNumbersList = np.array(savedValidNumbers)[:,0]
    ratioSums = 0
    for i in range(1, int(np.max(indices)+1)):
        print(validNumbersList[indices==i])
        ratio = validNumbersList[indices==i][0]*validNumbersList[indices==i][1]
        ratioSums += ratio

    print(int(ratioSums))


if __name__ == "__main__":
    main()