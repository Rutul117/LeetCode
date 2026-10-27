class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        grid.append("." * n)


        if m > 1:
            grid.append("#" * (n - 1) + '.')


        for i in range(2, m):
            grid.append(grid[1])


        return grid