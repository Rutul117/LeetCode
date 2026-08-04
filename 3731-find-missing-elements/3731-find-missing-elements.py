class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = nums[0]
        l = nums[0]
        for num in nums:
            if num > l:
                l = num
            elif num < s:
                s = num
        miss = []
        for num in range(s, l+1):
            if num not in nums:
                miss += [num]
        return miss