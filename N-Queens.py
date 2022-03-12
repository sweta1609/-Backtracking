def isSafe(row,col,board,n):
    #vertical direction
    i = row-1
    while i>= 0:
        if board[i][col] == 1:
            return False
        i -= 1
        
    #upper left diagonal
    i = row-1
    j = col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    #upper right diagonal
    i = row -1
    j = col +1
    while i >=0 and j<n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
        
    
       
    

def printPathHelper(row,n,board):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
        print()
        return
    for col in range(n):
        if isSafe(row,col,board,n):
            board[row][col] = 1
            printPathHelper(row+1,n,board)
            board[row][col] = 0 #after checking allrows when we come back we intiliase path as 0
    return
    
    
def nQueen(n):
    #Implement Your Code Here
    pass
    board = [[0 for i in range(n)]for j in range(n)]#initialise with 0
    printPathHelper(0,n,board)


n = int(input())
nQueen(n)

