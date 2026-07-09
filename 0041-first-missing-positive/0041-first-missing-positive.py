class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: place each number at its correct index
        i = 0
        while i < n:
            v = nums[i]
            if 1 <= v <= n and nums[v - 1] != v:
                nums[i], nums[v - 1] = nums[v - 1], nums[i]
            else:
                i += 1
        
        # Step 2: find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

