class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        def dp(nums: List[int]) -> int:

            n = len(nums)
            if n < 3: return 1
            root, left, right = nums[0], [], []

            for x in nums:
                if   x < root: left .append(x)
                elif x > root: right.append(x)

            return dp(left) * dp(right) * comb(n-1, len(left))

        return (dp(nums)-1) %1_000_000_007