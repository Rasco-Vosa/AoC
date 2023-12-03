import os

def main():
    filePath = os.path.join(os.path.dirname(__file__),'..', 'data', 'day2-input.txt')
    txtData = open(filePath,'r').read() 
    games = txtData.split('\n')
    games = list(filter(None, games))
    gameIndex = 0
    validGameIdsSum = 0
    for game in games:
        cubeSetData = game.split(':')[1].split(';')
        validGame = True
        gameIndex += 1
        for cubeSet in cubeSetData: 
            ListCubeSet = cubeSet.split(',') # List of values of cube set (still in string format)
            for cubeString in ListCubeSet:
                quantity, color = cubeString.strip().split(' ') #pairs (number of cubes, cube color)
                quantity = int(quantity)
                if (color == "red" and quantity > 12) or (color == "green" and quantity >13) or (color == "blue" and quantity >14):
                    validGame = False
        if validGame == True:
            validGameIdsSum +=gameIndex
            
    print("the final answer is: *Tatarara* ",validGameIdsSum)

if __name__ == "__main__":
    main()



