def move(board, startrow, startcol, endrow, endcol):
    ##import function should be at the top of your codes
    import copy
    newboard = copy.deepcopy(board)
    ##this is a move function which puts the pawn into a postion
    ##"=" means make the left eqauls to the value on right
    ##therefore it would work like this:
    ##destination = original position
    ##so I think what you want to do is 'end = start'
    ##and always comment your code like this
    ##really helpful for debugging
    newboard[startrow][startcol] = newboard[endrow][endcol]
    newboard[endrow][endcol] = 0
    print(newboard)

def generateMoves(color, board):
    ##always be careful with syntax errors
    ##python is very strict about that
    ##next line should've started at here
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if color == 2:
                    if i > 0 and board[i-1][j] == 0:
                        move(board, i, j, i - 1, j)
##                    board[i][j] = board[i-1][j]
##                    board[i-1][j] = 0
                    if i > 0 and j + 1 < len(board) and board[i-1][j+1] == 1:
                        move(board, i, j, i - 1, j + 1)
##                    board[i][j] = board[i-1][j+1]
##                    board[i-1][j+1] = 0
                    if i > 0 and j > 0 and board[i-1][j-1] == 1:
                        move(board, i, j, i - 1, j - 1)
##                    board[i][j] = board[i-1][j-1]
##                    board[i-1][j-1] = 0
                else:
                    if i < 2 and board[i+1][j] == 0:
                        move(board, i, j, i + 1, j)
##                    board[i][j] = board[i+1][j]
##                    board[i+1][j] = 0
                    if i < 2 and j + 1 < len(board) and board[i+1][j+1] == 2:
                        move(board, i, j, i + 1, j + 1)
##                    board[i][j] = board[i+1][j+1]
##                    board[i+1][j+1] = 0
                    if i < 2 and j > 0 and board[i+1][j-1] == 2:
                        move(board, i, j, i + 1, j - 1)
##                    board[i][j] = board[i+1][j-1]
##                    board[i+1][j-1] = 0
    ##you may want to handle more edge cases like if one side already won
    ##maybe not lol
    ##don't know what does the professor want
