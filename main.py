import random

print("Welcome to my Tic Tac Toe Game")
print("")
print("--------------------------------")
print("")

mapPositions = [1,2,3,4,5,6,7,8,9]
MapRows = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printMap():
    for x in range (rows):
        print("\n+---+---+---+")
        print("|", end ="")
        for y in range (cols):
            print("",MapRows[x][y], end =" |")
    print("\n+---+---+---+")
    
def modifArray(num, turn):
    num -= 1
    if(num == 0):
        MapRows[0][0]=turn
    elif(num == 1):
        MapRows[0][1]=turn
    elif(num == 2):
        MapRows[0][2]=turn
    elif(num == 3):
        MapRows[1][0]=turn
    elif(num == 4):
        MapRows[1][1]=turn
    elif(num == 5):
        MapRows[1][2]=turn
    elif(num == 6):
        MapRows[2][0]=turn
    elif(num == 7):
        MapRows[2][1]=turn
    elif(num == 8):
        MapRows[2][2]=turn

gameState = false 

turn = 'X'

turnCounter = 0

def checkWinner(MapRows):
    ### X axis
    if(MapRows[0][0] == 'X' and MapRows[0][1] == 'X' and MapRows[0][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[1][0] == 'X' and MapRows[1][1] == 'X' and MapRows[1][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[2][0] == 'X' and MapRows[2][1] == 'X' and MapRows[2][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][0] == 'Y' and MapRows[0][1] == 'Y' and MapRows[0][2] == 'Y'):
        print("Y has won")
        return "Y"
    elif(MapRows[1][0] == 'Y' and MapRows[1][1] == 'Y' and MapRows[1][2] == 'Y'):
        print("Y has won")
        return "Y"
    elif(MapRows[2][0] == 'Y' and MapRows[2][1] == 'Y' and MapRows[2][2] == 'Y'):
        print("Y has won")
        return "Y"
    ### Y axis"
    elif(MapRows[0][0] == 'X' and MapRows[1][0] == 'X' and MapRows[2][0] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][1] == 'X' and MapRows[1][1] == 'X' and MapRows[2][1] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][2] == 'X' and MapRows[1][2] == 'X' and MapRows[2][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][0] == 'Y' and MapRows[1][0] == 'Y' and MapRows[2][0] == 'Y'):
        print("Y has won")
        return "Y"
    elif(MapRows[0][1] == 'Y' and MapRows[1][1] == 'Y' and MapRows[2][1] == 'Y'):
        print("Y has won")
        return "Y"
    elif(MapRows[0][2] == 'Y' and MapRows[1][2] == 'Y' and MapRows[2][2] == 'Y'):
        print("Y has won")
        return "Y"
    ###Cross Win
    elif(MapRows[0][0] == 'Y' and MapRows[1][1] == 'Y' and MapRows[2][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][2] == 'Y' and MapRows[1][1] == 'Y' and MapRows[2][2] == 'X'):
        print("X has won")
        return "X"
    elif(MapRows[0][0] == 'Y' and MapRows[1][1] == 'Y' and MapRows[2][2] == 'Y'):
        print("Y has won")
        return "Y"
    elif(MapRows[0][2] == 'Y' and MapRows[1][1] == 'Y' and MapRows[2][2] == 'Y'):
        print("Y has won")
        return "Y"
    else:
        return "N" 
    

    