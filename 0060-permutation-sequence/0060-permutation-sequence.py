class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # zero-index the permutation space
        
        res = []
        for i in range(n, 0, -1):
            f = math.factorial(i - 1)
            idx = k // f
            res.append(nums.pop(idx))
            k %= f
        
        return "".join(res)
