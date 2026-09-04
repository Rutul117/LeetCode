class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                # If the middle element is greater than the element on its right, the peak must be on the left side including the middle element
                high = mid
            else:
                # If the middle element is less than the element on its right, the peak must be on the right side excluding the middle element
                low = mid + 1
        
        return low