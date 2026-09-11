class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        availableDigits = [0] * 10
        for d in digits:
            availableDigits[d] += 1
        
        res = 0

        for num in range(100, 1000, 2):
            digit1 = num // 100
            digit2 = (num // 10) % 10
            digit3 = num % 10

            availableDigits[digit1] -= 1
            availableDigits[digit2] -= 1
            availableDigits[digit3] -= 1

            if availableDigits[digit1] >= 0 and availableDigits[digit2] >= 0 and availableDigits[digit3] >= 0:
                res += 1
            
            availableDigits[digit1] += 1
            availableDigits[digit2] += 1
            availableDigits[digit3] += 1
        
        return res
