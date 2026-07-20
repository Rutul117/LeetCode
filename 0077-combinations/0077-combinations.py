class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int):
            # If the path is complete, commit it.
            if len(path) == k:
                res.append(path.copy())
                return
            
            # Pruning: if remaining numbers can't fill the quota, stop.
            # Available numbers = n - start + 1
            if len(path) + (n - start + 1) < k:
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return res
