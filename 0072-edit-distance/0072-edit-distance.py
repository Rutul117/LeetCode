class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0: return j  # Need to insert j chars
            if j == 0: return i  # Need to delete i chars
            if s1[i-1] == s2[j-1]:
                return dp(i-1, j-1)
            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        
        return dp(len(s1), len(s2))