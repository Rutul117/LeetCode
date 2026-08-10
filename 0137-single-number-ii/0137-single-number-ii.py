class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for x in nums:
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
        
        return ones
