import os

def main():
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day1-input.txt')
    rawData = open(filePath,'r').read() 
    parsedData = rawData.splitlines()
    calibrationValueSum = 0
    for txtLine in parsedData:
        index_store = []
        for i in range(0,len(txtLine)):
            if (txtLine[i].isdigit()):
                index_store.append(i) # store all indexes in each line that are algarism 
        calibrationValue = int(str(txtLine[min(index_store)]) + str(txtLine[max(index_store)])) # finding the calibration value for a line
        calibrationValueSum += calibrationValue 
    print("the final answer is: *Tatarara* ", calibrationValueSum)       


if __name__ == "__main__":
    main()
     


