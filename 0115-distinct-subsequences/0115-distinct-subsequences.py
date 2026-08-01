class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        total = 0
        def back(i, j):
            if (i,j) in dp: return dp[(i,j)]
            if j == len(t):
                return 1
            if i == len(s): return total
            ans = back(i+1, j)
            if s[i] == t[j]:
                ans += back(i+1, j+1)
            dp[(i, j)] = ans
            return ans
        return back(0, 0)