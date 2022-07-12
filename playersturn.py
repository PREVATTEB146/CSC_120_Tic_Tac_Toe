gameboard = [ "-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
print("Hello user, here is the game board you will be playing on today! As always good luck and have fun!")
def printboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print("")
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print("")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])
print("Player 1 will be X and player two will be O. Play fair and have fun!")
player = "X"
gameActive = True
win = None

# players making input selections.
def playerselect(gameboard):
    select = int(input("Please select a number 0-8:"))
    if select >= 0 and select < 9 and gameboard[select] == "-":
        gameboard[select] = player
    else:
        print("Sorry but you can not place your marker at this spot, please try again.")

#switching people
def switching():
    global player
    if player == "X":
        player = "0"
    else:
        player = "X"



while gameActive:
    printboard(gameboard)
    playerselect(gameboard)
