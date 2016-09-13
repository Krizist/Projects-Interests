import copy
def move(board, startrow, startcol, endrow, endcol):
    newboard = copy.deepcopy(board)
    newboard[endrow][endcol] = newboard[startrow][startcol]
    newboard[startrow][startcol] = 0
    return newboard

def generateMoves(color, board):
    ##throw exception
    if color == 0:
        print "color cannot be 0"
        return
    ##create the list to return
    mlist = []
    enemies = 0
    row = 0
    for l in board:
        ##refresh column for each new row
        col = 0
        for i in l:
            if i == color:
                ##if controlling a non-white pawn but already at row 0
                ##win! do what you want to do like printing a win message
                if color != 1 and row == 0:
                    print "already won"
                ##if controlling a white pawn and not reach top row yet
                elif color != 1 and row > 0:
                    if board[row - 1][col] == 0:
                        mlist.append(move(board, row, col, row-1, col))
                    if col > 0 and board[row - 1][col - 1] == 1:
                        mlist.append(move(board, row, col, row-1, col-1))
                    if col < len(board)-1 and board[row - 1][col + 1] == 1:
                        mlist.append(move(board, row, col, row-1, col+1))
                ##if controlling a while pawn and reached the bottom line
                ##win!
                elif row == 2:
                    print "already won"
                ##control a while pawn but not reach bottom row yet
                else:
                    if board[row + 1][col] == 0:
                        mlist.append(move(board, row, col, row+1, col))
                    if col > 0 and board[row + 1][col - 1] == 2:
                        mlist.append(move(board, row, col, row+1, col-1))
                    if col < len(board)-1 and board[row + 1][col + 1] == 2:
                        mlist.append(move(board, row, col, row+1, col+1))
            ##count for enemies
            elif i != 0:
                enemies += 1
            ##add column after permutating each elements in rows
            col += 1
        ##add row after permutation of every list in board
        row += 1
    ##check if you win
    if enemies == 0:
        return
    print mlist
    return mlist

def chooseBestMoves(color, mlist):
    listN = []
    dic={}
    enemies = 0
    mine = 0
    kill = 0
    block = 0
    for listNum in range(0, len(mlist)):
        rowTotal = 0
        for row in range(0, len(mlist[0])):
            col = 0
            for b in mlist[listNum][row]:
                if b != color and b != 0:
                    enemies += 1
                    templist = mlist[listNum]
                    #Bloooooooock
                    dic = dict(dic)
                    if listNum not in dic.keys():
                        dic[listNum] = 0
                    if color == 2:
                        if templist[row+1][col] == color:
                            dic[listNum] += 2
                    elif color == 1:
                        if templist[col][row-1] == color:
                            dic[listNum] += 2
                    #try not to be killed
                    if col == 0 and templist[row][col + 1] != (color or 0):
                        dic[listNum] -= 1
                    elif col == len(templist[row])-1 and templist[row][col-1] != (color or 0):
                        dic[listNum] -= 1
                elif b == color:
                    if row == 0 and color == 2 and b == color:
                        return mlist[listNum]
                    elif row == len(mlist[0])-1 and color == 1 and b == color:
                        return mlist[listNum]
                    mine+=1
                col+=1
            rowTotal += sum(mlist[listNum][row])
        listN += [rowTotal]
        for i in range(1, len(listN)):
            if listN[i] < listN[0]:
                kill = i
    if kill != 0:
        return mlist[kill]
    else :
        for i in listN:
            if i > listN[0]:
                return mlist[kill]
    dic = sorted(dic.items(), key = lambda dic:dic[1], reverse = True)
    if dic != []:
        t = list(dic[0])[0]
        return mlist[t]


##############TEST AT HERE#################
def main():
    ##generateMoves(2, [[0,1,1],[1,0,0],[2,2,2]])
    ##test 1:
    print "Test 1"
    print chooseBestMoves(2, generateMoves(2, [[0,1,1],[1,0,0],[2,2,2]]))
    # ##print "Choose Best Moves"
    print chooseBestMoves(1, generateMoves(1, [[0,1,1],[2,0,0],[2,0,2]]))
    # ##print "Choose Best Moves"
    print chooseBestMoves(2, generateMoves(2, [[0,0,1],[1,0,0],[2,0,0]]))
    ##test 2:
    print "Test 2"
    ##step 1:
    print chooseBestMoves(2, generateMoves(2, [[1,0,1],[0,1,0],[2,2,2]]))
    print chooseBestMoves(1, generateMoves(1, [[1, 0, 1], [0, 2, 0], [2, 2, 0]]))
    print chooseBestMoves(2, generateMoves(2, [[1, 0, 0], [0, 1, 0], [2, 2, 0]]))
    print chooseBestMoves(1, generateMoves(1, [[1, 0, 0], [0, 2, 0], [0, 2, 0]]))
    print chooseBestMoves(2, generateMoves(2, [[0, 0, 0], [0, 1, 0], [0, 2, 0]]))
    print "Test 3"
    ##step 1:
    print chooseBestMoves(2, generateMoves(2, [[1,1,1, 1],[0,0,0,0],[0,0,0,2],[2, 2, 2, 0]]))
    print chooseBestMoves(1, generateMoves(1, [[1, 1, 1, 1], [0, 0, 0, 2], [0, 0, 0, 0], [2, 2, 2, 0]]))
main()
