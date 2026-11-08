class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Step 1: Initialize variables
        rows = len(grid)
        cols = len(grid[0])
        
        # Step 2: Count servers in each row and column
        row_count = [0] * rows
        col_count = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Step 3: Count servers that can communicate
        total_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # A server can communicate if there is another server
                    # in the same row or column
                    if row_count[i] > 1 or col_count[j] > 1:
                        total_servers += 1
        
        return total_servers
