# Assume that you have functions to check if a given space is free (isSpaceFree)
# a copy of the board you can test different moves on (boardCopy), a function to
# make a given move (makeMove), a function to check to see if you won (isWinner)
# and a function that randomly selects a valid move from a given set of moves
# (chooseRandomMoveFromList).

# The signatures for each of the given functions are as follows
# isSpaceFree(string[] boardCopy, int i)
# getBoardCopy(string[] board)
# makeMove(string[] boardCopy, string letter, int move)
# isWinner(string[] board, string letter)
# chooseRandomMoveFromList(string[] board, int[] moveList)

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #TODO: Check to see if we can win in the next move. Make a copy of the board
    #and check each space to see if a) it's open, and b)whether it will win the
    #game. If you find a move that will win the game, return it.

    #TODO: Check if the other player could win on his next move. This will look
    #almost identical, only you are checking if the player can win, not the
    #computer.

    #TODO: Try to take one of the corners, it they are free. You will need to
    #give it the corners and have it select a random valid move from that list

    #TODO: Try to take the center if it is free. This is the same as above, only
    #you will need to give it a different space

    #TODO: Try to take the sides. This is the same as above, only with a
    #different list passed in
