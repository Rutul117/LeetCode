class Solution(object):
    def maxSubarrayLength(self, nums, k):
        i = j = 0
        n = len(nums)
        ans = 1
        frequency_map = {}

        while i < n:
            frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1
            while frequency_map[nums[i]] > k:
                frequency_map[nums[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
            i += 1
        return ans
