from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        inc_len = 1
        dec_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Strictly increasing
                inc_len += 1
                dec_len = 1  # Reset decreasing length
            elif nums[i] < nums[i - 1]:  # Strictly decreasing
                dec_len += 1
                inc_len = 1  # Reset increasing length
            else:  # Neither increasing nor decreasing
                inc_len = 1
                dec_len = 1
            
            longest = max(longest, inc_len, dec_len)
        
        return longest
