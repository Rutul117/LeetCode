class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))  # remove duplicates

        longest = 1
        current = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] == sorted_nums[i] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        longest = max(longest, current)
        return longest