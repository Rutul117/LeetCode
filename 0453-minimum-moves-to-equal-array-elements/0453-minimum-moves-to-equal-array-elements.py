class Solution:
    def minMoves(self, a: list[int]) -> int:
        mn = min(a)
        return sum(x-mn for x in a)