import os
import numpy as np

def main():
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day4-input.txt')
    rawData = open(filePath,'r').read() 
    parsedData = list(filter(None, rawData.replace("Card","").replace(":","|").splitlines()))

    nRows = int(len(parsedData))
    availableCards = np.ones((nRows, 1))
    i = 0
    for card in parsedData: 
        cardArray = card.split("|")
        cardWinNumbers = np.array([int(x) for x in cardArray[1].strip().split()])
        cardMyNumbers = np.array([int(x) for x in cardArray[2].strip().split()])
        nMatchNumbers = len(np.intersect1d(cardMyNumbers,cardWinNumbers))

        # calculate what to add from 1 card
        copyCard = np.zeros((nRows, 1))
        copyCard[i+1:i+nMatchNumbers+1] = 1

        # adding new card possibilities to available cards
        availableCards += copyCard*availableCards[i]
        i += 1
    
    print(int(np.sum(availableCards)))


if __name__ == "__main__":
    main()
     

