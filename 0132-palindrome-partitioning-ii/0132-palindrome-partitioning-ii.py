class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = [i for i in range(n)] 

        for center in range(n):
            left, right = center, center
            while left >= 0 and right < n and s[left] == s[right]:
                cuts[right] = 0 if left == 0 else min(cuts[right], cuts[left - 1] + 1)
                left -= 1
                right += 1

            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                cuts[right] = 0 if left == 0 else min(cuts[right], cuts[left - 1] + 1)
                left -= 1
                right += 1

        return cuts[-1]