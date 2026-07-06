class Solution:
    def removeCoveredIntervals(self, a: List[List[int]]) -> int:
        R = 0
        return sum(R<(R:=max(R,-r)) for l,r in sorted((l,-r) for l,r in a))