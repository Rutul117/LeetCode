class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'  # Mark as visited
            
            # Check all neighboring cells
            found = (dfs(row + 1, col, index + 1) or
                     dfs(row - 1, col, index + 1) or
                     dfs(row, col + 1, index + 1) or
                     dfs(row, col - 1, index + 1))
            
            board[row][col] = temp  # Reset
            
            return found
        
        # Start search from each cell
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False

# Example usage:
board1 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word1 = "ABCCED"

board2 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word2 = "SEE"

board3 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word3 = "ABCB"