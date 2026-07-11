class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Make a copy of the current permutation
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recur for the next position
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo the swap)

        result = []
        backtrack(0)
        return result