class Solution(object):
    def majorityElement(self, nums):
        count = 0
        result = 0
        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count += 1
            else:
                count -= 1
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        