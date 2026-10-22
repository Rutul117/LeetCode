class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n, a = len(nums), nums[0]
        ans = float('inf')

        if all(nums[i] == (a + i) % n for i in range(n)):
            ans = 0 if a == 0 else min(n - a, a + 2)

        if all(nums[i] == (a - i) % n for i in range(n)):
            k = (a + 1) % n
            ans = min(ans, 1 + (n - k) % n, k + 1)

        return -1 if ans == float('inf') else ans