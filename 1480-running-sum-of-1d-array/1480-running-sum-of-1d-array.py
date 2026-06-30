class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        res = []
        for i in range(len(nums)):
            summ += nums[i]
            res.append(summ)

        return res