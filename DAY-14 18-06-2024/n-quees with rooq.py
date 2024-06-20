'''
ip:
   6*6-->square matrix
   (2,3)-->rooq position
  
   - - - - - r     q - - - - -
   q - - - - -     - - q - - -
   - - q - - -     - - - r - -
   - - - - q -     - - - - - q
   - q - - - -     - q - - - - 
   - - - q - -     - - - - q -
   
   queen(q) cannot be placed in same row,col,diagnol
   if rooq(elephant) present in any of the row the queen can't be placed in the row and col
'''

def is_valid(board, row, col, n):
    for i in range(col):# check horizontal
        if board[row][i] == 'q':
            return False
    i = row
    j = col
    while i>=0 and j >= 0: # upper left diag
        if board[i][j] == 'q':
            return False
        i -= 1 
        j -= 1 
    i = row
    j = col
    while i<n and j >=0: #bottom left diag
        if board[i][j] == 'q':
            return False
        i += 1 
        j -= 1
        
    return True
def solve(n):
    board = [['-' for i in range(n)] for j in range(n)]
    def backtrack(col):
        if col == n:
            return True
        for i in range(n):
            if is_valid(board, i, col, n):
                board[i][col] = 'q'
                
                if backtrack(col+1):
                    return True
                
                board[i][col] = '-'
        
        return False
    
    if backtrack(0):
        for row in board:
            print("".join(row))
    else:
        print("no solution")
n = int(input())
solve(n)


