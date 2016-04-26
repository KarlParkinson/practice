import time

def whoWins(board):
    leftCornerRow = (len(board) - 1) / 2
    leftCornerColumn = (len(board) - 1) / 2

    region = 1
    while (leftCornerRow >= 0):
        winner = squareCheck(leftCornerRow, leftCornerColumn, region, board)
        if (winner != 'Draw'):
            return winner
        else:
            leftCornerRow -= 1
            leftCornerColumn -=1
            region += 1
    return 'Draw'


def squareCheck(startRow, startColumn, regionNum, board):
    forward = (regionNum * 2) - 1
    i = startRow
    j = startColumn
    aliceCount = 0
    bobCount = 0

    
    end = j + forward
    while (j < end):
        if (board[i][j] == 'A'):
            aliceCount += 1
        elif (board[i][j] == 'B'):
            bobCount += 1
        j += 1

    end = i + forward
    while (i < end):
        if (board[i][j] == 'A'):
            aliceCount += 1
        elif (board[i][j] == 'B'):
            bobCount += 1
        i += 1

    end = j - forward
    while (j > end):
        if (board[i][j] == 'A'):
            aliceCount += 1
        elif (board[i][j] == 'B'):
            bobCount += 1
        j -= 1

    end = i - forward
    while (i > end):
        if (board[i][j] == 'A'):
            aliceCount += 1
        elif (board[i][j] == 'B'):
            bobCount += 1
        i -= 1

    if (aliceCount > bobCount):
        return 'Alice'
    elif(bobCount > aliceCount):
        return 'Bob'
    else:
        return 'Draw'
        


board= []
for i in range(0,50):
    s = ""
    for j in range(0,50):
        s += "."
    board.append(s)
print len(board)
t = time.time()
print whoWins(board)
print("--- %s ---" % (time.time() - t))
