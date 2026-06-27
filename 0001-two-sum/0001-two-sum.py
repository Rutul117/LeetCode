class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums:
                j = nums.index(complement)

                if i != j:
                    return [j, i]

        return []