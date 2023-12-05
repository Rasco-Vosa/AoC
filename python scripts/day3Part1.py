import os
import numpy as np
import matplotlib.pyplot as plt

def main (): 
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day3-input.txt')
    txtData = open(filePath,'r').read()
    
    # Convert array to matrix of 0,1,2 
    npArray = np.array([list(row) for row in txtData.split('\n')])
    convArray = np.select([npArray == '.', np.char.isdigit(npArray), npArray == '*'], [0, 1, 3], default=2)
    

    #setting import Mask variables and indexes of symbols 
    symbolMaskIndexes = np.where(convArray == 2)
    AlldigitMask = (convArray == 1)
    symbolNeighboursMask = np.zeros(np.shape(convArray), dtype=bool)
    #create mask for positions around symbols
    for i in range(0, np.shape(symbolMaskIndexes)[1]):
            # This logic is enough assuming that none of the symbols is on the outter layer (which was checked)
            symbolNeighboursMask[symbolMaskIndexes[0][i]-1:symbolMaskIndexes[0][i]+2, symbolMaskIndexes[1][i]-1:symbolMaskIndexes[1][i]+2] = True
    #Mask with Digits that are in contact with symbols
    contactDigits = symbolNeighboursMask*AlldigitMask

    # Looking for valid numbers ==> numbers which have a "contactDigit"
    savedValidNumbers = []
    for i in range(0, np.shape(convArray)[0]):
         numb = ""
         validNumber = False
         for j in range(0, np.shape(convArray)[1]):
            if convArray[i,j] == 1:
                numb = numb + npArray[i,j]
                if (contactDigits[i,j] == True): validNumber = True

                if j<np.shape(convArray)[1]-1:
                    if ((convArray[i,j+1] != 1)): 
                        if validNumber == True: savedValidNumbers.append(int(numb))
                        numb = ""
                        validNumber = False
                else:
                    if (validNumber == True): 
                        savedValidNumbers.append(int(numb))
                        numb = ""
                        validNumber = False
    print(np.sum(savedValidNumbers))

if __name__ == "__main__":
    main()