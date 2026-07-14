class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest_reachable = 0
        
        for i in range(len(nums)):
            if i > furthest_reachable:
                return False
            furthest_reachable = max(furthest_reachable, i + nums[i])
        
        return True
