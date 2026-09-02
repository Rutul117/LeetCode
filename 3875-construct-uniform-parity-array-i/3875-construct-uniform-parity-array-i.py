class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        eve_count, odd_count = 0, 0

        for num in nums1:
            if num % 2 == 0:
                eve_count += 1
            else:
                odd_count += 1

        if eve_count == 0 or odd_count == 0 or eve_count >= 1 or odd_count >= 1:
            return True

        return False