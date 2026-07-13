
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the variables
        max_current = nums[0]  # max sum of subarray ending at current position
        max_global = nums[0]   # max sum found so far
        
        for i in range(1, len(nums)):
            # Update the maximum subarray sum ending at current position
            max_current = max(nums[i], max_current + nums[i])
            # Update the global maximum subarray sum
            if max_current > max_global:
                max_global = max_current
        
        return max_global