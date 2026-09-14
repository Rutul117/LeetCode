from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: [start, end, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by start time
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose start > arr[i].end
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best answer using intervals from i onward
        # with at most k intervals remaining.
        #
        # Each state stores:
        # (total_weight, tuple_of_original_indices)
        dp = [[None] * 5 for _ in range(n + 1)]

        for k in range(5):
            dp[n][k] = (0, ())

        def better(a, b):
            """Return the better of two states."""
            if a is None:
                return b
            if b is None:
                return a

            # Higher score is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: skip current interval
                skip = dp[i + 1][k]

                # Option 2: take current interval
                weight = arr[i][2]
                index = arr[i][3]

                take_next = dp[nxt[i]][k - 1]
                take = (
                    weight + take_next[0],
                    tuple(sorted((index,) + take_next[1]))
                )

                dp[i][k] = better(skip, take)

            # With 0 intervals allowed, score is 0
            dp[i][0] = (0, ())

        return list(dp[0][4][1])