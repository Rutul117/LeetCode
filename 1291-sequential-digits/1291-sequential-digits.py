class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []

        for start_digit in range(1, 9):
            num = start_digit
            next_digit = start_digit + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                next_digit += 1

        return sorted(result)
