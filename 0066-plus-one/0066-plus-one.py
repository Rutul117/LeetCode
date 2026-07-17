class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate from the last digit backwards
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no cascading carry
            digits[i] = 0  # carry forward
        
        # if we reach here, all digits were 9
        return [1] + digits