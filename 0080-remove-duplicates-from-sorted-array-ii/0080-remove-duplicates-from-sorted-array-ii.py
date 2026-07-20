class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1  # Pointer for the position to place next unique element
        
        # Initialize count to keep track of occurrences of current element
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for new element
            
            if count <= 2:  # Check if the count is less than or equal to 2
                nums[k] = nums[i]
                k += 1
        
        return k
