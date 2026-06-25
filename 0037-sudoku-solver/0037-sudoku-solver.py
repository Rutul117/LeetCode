class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = defaultdict(set), defaultdict(set)
        grids = defaultdict(set)

        one_nine = set([str(i) for i in range(1, 10)])
        fill = [] # '.' to fill
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[(r // 3, c // 3)].add(board[r][c])
                else:
                    fill.append((r, c))
        
        def dfs(i):
            if i == len(fill):
                return True
            r, c = fill[i]
            options = one_nine - rows[r] - cols[c] - grids[(r // 3, c // 3)] 
            if not options: # can't find any number to fill in
                return False
            for op in options:
                rows[r].add(op)
                cols[c].add(op)
                grids[(r // 3, c // 3)].add(op)
                board[r][c] = op
                if not dfs(i + 1): # fill in the 'op' doesn't work out, backtrack
                    rows[r].remove(op)
                    cols[c].remove(op)
                    grids[(r // 3, c // 3)].remove(op)
                    board[r][c] = '.'
                else:
                    break
            else: # no number in options work out, this path is wrong
                return False
            return True
        dfs(0)