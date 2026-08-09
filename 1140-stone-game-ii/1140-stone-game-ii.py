class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        # Create a memoization table
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # Create a suffix sum array to calculate the sum of stones from i to end
        suffixSum = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + piles[i]
        
        def dfs(i, M):
            # If all piles are taken
            if i == n:
                return 0
            # If the result is already computed
            if dp[i][M] != 0:
                return dp[i][M]
            # Max stones Alice can take starting from index i with M
            maxStones = 0
            # Try taking 1 to 2*M piles
            for x in range(1, 2 * M + 1):
                if i + x > n:
                    break
                # Maximize Alice's stones by minimizing what Bob can take
                maxStones = max(maxStones, suffixSum[i] - dfs(i + x, max(M, x)))
            dp[i][M] = maxStones
            return dp[i][M]
        
        return dfs(0, 1)