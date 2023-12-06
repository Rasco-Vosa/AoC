import os
import numpy as np

def main():
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day4-input.txt')
    rawData = open(filePath,'r').read() 
    parsedData = list(filter(None, rawData.replace("Card","").replace(":","|").splitlines()))
    print(parsedData)

    cardNumberSum = 0
    for card in parsedData: 
        cardArray = card.split("|")
        cardNumber = cardArray[0].replace(" ","")
        cardWinNumbers = np.array([int(x) for x in cardArray[1].strip().split()])
        cardMyNumbers = np.array([int(x) for x in cardArray[2].strip().split()])
        nMatchNumbers = len(np.intersect1d(cardMyNumbers,cardWinNumbers))
        
        if nMatchNumbers > 0:
            cardScore = 2**(nMatchNumbers-1)
        elif nMatchNumbers == 0:
            cardScore = 0
        else:
            print("This should not happen")
        
        cardNumberSum += cardScore
    print(cardNumberSum)

if __name__ == "__main__":
    main()
     

