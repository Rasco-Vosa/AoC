import numpy as np

def find_all_occurrences(string, substring):
    indices = []
    start_index = 0

    for _ in range(string.count(substring)):
        index = string.find(substring, start_index)
        if index != -1:
            indices.append(index)
            start_index = index + 1

    return indices

rawData = open('day1-input.txt','r').read() 
parsedData = rawData.splitlines()
calibrationValueSum = 0
nWrittenFull = np.array([["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9]])

for txtLine in parsedData:
    indexAndDigit = []

    # Search for all digits and their position
    for i in range(0,len(txtLine)):
        if (txtLine[i].isdigit()):
            indexAndDigit.append([i,int(txtLine[i])]) # store all indexes in each line that are numeric single digits

    # Search for all written numbers and their position
    for j in range(0,len(nWrittenFull)):
        numb_index = find_all_occurrences(txtLine, nWrittenFull[j][0])
        for i in range(0,len(numb_index)):
            if numb_index[i]>=0:
                indexAndDigit.append([numb_index[i], int(nWrittenFull[j][1])])
    
    
    firstIndex = np.argmin(np.array(indexAndDigit)[:,0])
    LastIndex = np.argmax(np.array(indexAndDigit)[:,0])
    FirstDigit = np.array(indexAndDigit)[:,1][firstIndex]
    LastDigit = np.array(indexAndDigit)[:,1][LastIndex]

    calibrationValue = int(str(FirstDigit) + str(LastDigit)) # finding the calibration value for a line
    #print(calibrationValue)
    calibrationValueSum += calibrationValue

print(calibrationValueSum)

    
            

"""     firstDigit = int(txtLine[min(index_store)])
    lastDigit = int(txtLine[max(index_store)])
    firstIndex = index_store[0]
    lastIndex = index_store[-1]

    for j in range(0,len(nWrittenFull)):
        startSearch = txtLine[0:index_store[0]].find(nWrittenFull[j])
        endSearch = txtLine[index_store[-1]:].find(nWrittenFull[j])
        if startSearch >= 0 and startSearch < firstIndex:
            firstIndex = startSearch
            firstDigit = j+1 
        if endSearch >= 0 and endSearch > lastIndex: 
            lastIndex = endSearch
            lastDigit = j+1  """
            

"""     calibrationValue = int((str(firstDigit)) + str(lastDigit)) # finding the calibration value for a line
    calibrationValueSum += calibrationValue 
print("the final answer is: *Tatarara* " + str(calibrationValueSum))         """


