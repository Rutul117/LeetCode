class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = chain([{0}], repeat(set()))
        for row in grid:
            left = set()
            dp = [left := {*map(v.__xor__, above | left)}
                  for above, v in zip(dp, row)]
        return min(dp[-1])