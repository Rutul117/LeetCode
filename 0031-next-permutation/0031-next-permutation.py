from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        ind = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:  # Find breakpoint
                ind = i
                break
        
        if ind == -1:
            # If no such index is found, reverse the array (smallest permutation)
            nums.reverse()
            return
        
        # Step 2: Find the element just larger than nums[ind] from the right
        for i in range(length - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]  # Swap
                break
        
        # Step 3: Reverse the part after ind
        nums[ind + 1:] = reversed(nums[ind + 1:])


        