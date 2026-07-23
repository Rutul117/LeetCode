class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1 or n == 2:
            return n

        else:
            m = max(nums)
            k = m.bit_length()

            return (2 ** k)
        