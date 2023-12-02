rawData = open('Day1-input.txt','r').read()
parsedData = rawData.splitlines()
calibrationValueSum = 0
for txtLine in parsedData:
    index_store = []
    for i in range(0,len(txtLine)):
        if (txtLine[i].isdigit()):
            index_store.append(i)
    calibrationValue = int(str(txtLine[min(index_store)]) + str(txtLine[max(index_store)]));
    calibrationValueSum += calibrationValue
print("the final answer is: *Tatarara *" + str(calibrationValueSum))        


