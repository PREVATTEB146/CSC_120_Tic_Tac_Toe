gameboard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
player = "X"
gameActive = True
win = None

print("Hello user, here is the game board you will be playing on today! As always good luck and have fun!")
def printboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print("")
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print("")
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])


print("Player 1 will be X and player two will be O. Play fair and have fun!")


def placemark(gameboard):
    select = int(input("Please select a number 0-8:"))
    if 0 <= select < 9 and gameboard[select] == "-":
        gameboard[select] = player
    else:
        print("Sorry but you can not place your marker at this spot, please try again.")
def checkrow(gameboard):
    global win
    if gameboard[0] == gameboard[1] == gameboard[2] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[3] == gameboard[4] == gameboard[5] and gameboard[3] != "-":
        win = gameboard[3]
        return True
    elif gameboard[6] == gameboard[7] == gameboard[8] and gameboard[6] != "-":
        win = gameboard[6]
        return True
def checkcol(gameboard):
    global win
    if gameboard[0] == gameboard[3] == gameboard[6] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[1] == gameboard[4] == gameboard[7] and gameboard[1] != "-":
        win = gameboard[1]
        return True
    elif gameboard[2] == gameboard[5] == gameboard[8] and gameboard[2] != "-":
        win = gameboard[2]
        return True
def checkcross(gameboard):
    global win
    if gameboard[0] == gameboard[4] == gameboard[8] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[2] == gameboard[4] == gameboard[6] and gameboard[2] != "-":
        win = gameboard[2]
        return True
def checkfortie(gameboard):
    global gameActive
    if "-" not in gameboard:
        print(
            "It seems like you two are an even match because there is a tie! Please play again for another shot at glory.")
        gameActive = False
def winner():
    global gameActive
    if checkcross(gameboard) or checkcol(gameboard) or checkrow(gameboard):
        print("The winner is " + str(win))
        print("Please come back again to settle the score whenever you would like.")
        gameActive = False
def switching(gameboard):
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

while gameActive:
    printboard(gameboard)
    placemark(gameboard)
    checkfortie(gameboard)
    winner()
    switching(gameboard)

