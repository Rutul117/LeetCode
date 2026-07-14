from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for x in nums:
            next_dp = [row[:] for row in dp]
            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    if not dp[g1][g2]: continue
                    n1, n2 = gcd(g1, x), gcd(g2, x)
                    # add x to S1
                    next_dp[n1][g2] = (next_dp[n1][g2] + dp[g1][g2]) % MOD
                    # add x to S2
                    next_dp[g1][n2] = (next_dp[g1][n2] + dp[g1][g2]) % MOD
            dp = next_dp

        return sum(dp[g][g] for g in range(1, m + 1)) % MOD