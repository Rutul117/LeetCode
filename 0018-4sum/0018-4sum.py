class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n - 3):
            # Skip duplicate first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                lo, hi = j + 1, n - 1

                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if total == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])

                        lo += 1
                        hi -= 1

                        # Skip duplicates
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

                    elif total < target:
                        lo += 1
                    else:
                        hi -= 1

        return answer