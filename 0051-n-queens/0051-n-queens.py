class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def NQueens(board, row):
            if row==len(board):
                ans = display(board)
                res.append(ans)
                return
                

            for col in range(len(board)):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    NQueens(board, row+1)
                    board[row][col] = '.'
                    

        def isSafe(board, row, col):
            # vertical up
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # diagonal left
            maxLeft = min(row, col)
            for i in range(1, maxLeft+1):
                if board[row-i][col-i] == 'Q':
                    return False
                    
            # diagonal right
            maxRight = min(row, len(board)-col-1)
            for i in range(1, maxRight+1):
                if board[row-i][col+i] == 'Q':
                    return False

            return True


        def display(board):
            temp = []
            for row in board:
                temp.append(''.join(row))
            return temp


        def matrix(r,c,value):
            return [[value for _ in range(c)] for _ in range(r)]

        board = matrix(n,n,'.')
        NQueens(board, 0)
        return res

        

                
         

    