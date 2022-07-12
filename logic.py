#Checking for wins and ties
gameActive = True
win = None
def checkrow(gameboard):
    global win
    if gameboard[0] == gameboard [1] == gameboard[2] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[3] == gameboard [4] == gameboard[5] and gameboard[3] != "-":
        win = gameboard[3]
        return True
    elif gameboard[6] == gameboard [7] == gameboard[8] and gameboard[6] != "-":
        win = gameboard[6]
        return True

def checkcol(gameboard):
    global win
    if gameboard[0] == gameboard [3] == gameboard[6] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[1] == gameboard [4] == gameboard[7] and gameboard[1] != "-":
        win = gameboard[1]
        return True
    elif gameboard[2] == gameboard [5] == gameboard[8] and gameboard[2] != "-":
        win = gameboard[2]
        return True

def checkcross(gameboard):
    global win
    if gameboard[0] == gameboard [4] == gameboard[8] and gameboard[0] != "-":
        win = gameboard[0]
        return True
    elif gameboard[2] == gameboard [4] == gameboard[6] and gameboard[2] != "-":
        win = gameboard[2]
        return True

#checking tie
def checkfortie(gameboard):
    global gameActive
    if "-" not in gameboard:
        print("It seems like you two are an even match because there is a tie! Please play again for another shot at glory.")
        gameActive = False

# checking a winner
def winner():
    global gameActive
    if checkcross(gameboard) or checkcol(gameboard) or checkrow(gameboard):
        print("The winner is " + win)
        gameActive = False


