class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        left_q = 0
        right_q = 0

        for i in range(n // 2):
            if num[i] == '?':
                left_q += 1
            else:
                diff += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                right_q += 1
            else:
                diff -= int(num[i])
                
        if (left_q + right_q) % 2 == 1:
            return True
        return diff != 9 * (right_q - left_q) // 2