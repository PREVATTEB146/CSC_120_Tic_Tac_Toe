gameboard = [ "-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
print( "Hello user, here is the game board you will be playing on today! As always good luck and have fun!")
def printboard(gameboard):
    print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2])
    print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5])
    print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8])
printboard(gameboard)
