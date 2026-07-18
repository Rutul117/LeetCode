class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        # Euclid's algorithm
        while mx % mn != 0:
            mx, mn = mn, mx % mn
        
        return mn
