class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n, ans = len(nums), 0

        for i in range(n):
            cnt = 0

            for j in range(i, n):
                if nums[j] == target: cnt += 1

                if 2 * cnt > j - i + 1:
                    ans += 1

        return ans