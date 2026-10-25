class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
        count = 0

        def dfs(row, column):
            if grid[row][column] == 0:
                grid[row][column] = 1
                if row >= 1:
                    dfs(row-1, column)
                if row+1 < num_rows:
                    dfs(row+1, column)
                if column >= 1:
                    dfs(row, column-1)
                if column+1 < num_columns:
                    dfs(row, column+1)                
                
        
        for r in range(num_rows):
            dfs(r, 0)
            dfs(r, num_columns-1)
        for c in range(num_columns):
            dfs(0, c)
            dfs(num_rows -1 , c)

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r,c)
        
        return count