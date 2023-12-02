txtData = open('day2-input.txt','r').read()
games = txtData.split('\n')
games = list(filter(None, games))
gameIndex = 0
FullPower = 0 # power of all games added

for game in games:
    cubeSetData = game.split(':')[1].split(';')
    gameIndex += 1
    minRed = 0
    minGreen = 0
    minBlue = 0
    for cubeSet in cubeSetData: 
        ListCubeSet = cubeSet.split(',') # List of values of cube set (still in string format)
        for cubeString in ListCubeSet:
            quantity, color = cubeString.strip().split(' ') #pairs (number of cubes, cube color)
            quantity = int(quantity)
            if (color == "red" and quantity>minRed):
                minRed = quantity
            elif(color == "green" and quantity>minGreen):
                minGreen = quantity
            elif(color == "blue" and quantity>minBlue):
                minBlue = quantity

    cubeSetpower = minRed*minBlue*minGreen
    FullPower += cubeSetpower

print(FullPower)



