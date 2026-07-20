class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Add the current subset (path) to the result
            for i in range(start, len(nums)):
                # Include nums[i] into the current subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack by removing nums[i]
                path.pop()
        
        backtrack(0, [])
        return result
