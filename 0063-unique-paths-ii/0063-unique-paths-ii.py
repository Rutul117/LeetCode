class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return 0
        m, n = len(grid), len(grid[0])
        lst = [0] * n
        lst[0] = 1
        for j in range(1, n):
            if grid[0][j]:
                break
            else:
                lst[j] = 1
        for i in range(1, m):
            if grid[i][0]:
                lst[0] = 0
            for j in range(1, n):
                if grid[i][j]:
                    lst[j] = 0
                else:
                    lst[j] += lst[j-1]
        return lst[-1] 