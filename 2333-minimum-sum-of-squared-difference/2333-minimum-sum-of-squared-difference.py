class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:
        """
        Minimize sum((nums1[i] - nums2[i])^2) after at most k1+k2 total
        ±1 adjustments to elements of nums1 or nums2.

        Strategy:
        - Work with absolute differences only.
        - Always reduce the largest difference first
          (greedy optimality for convex square cost).
        - Use a counting array to efficiently track how many
          differences have each magnitude.
        """

        # Total number of allowed operations
        k = k1 + k2

        # Absolute pairwise differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        # If total differences can be fully eliminated
        if sum(diffs) <= k:
            return 0

        # Maximum observed difference
        m = max(diffs)

        # Frequency array: cnt[v] = number of differences equal to v
        cnt = [0] * (m + 1)
        for d in diffs:
            cnt[d] += 1

        # Greedily reduce largest differences first
        for v in range(m, 0, -1):
            if k == 0:
                break

            c = cnt[v]
            if c == 0:
                continue

            if k >= c:
                # Reduce all differences of size v to v-1
                cnt[v] = 0
                cnt[v - 1] += c
                k -= c
            else:
                # Reduce only k of them
                cnt[v] -= k
                cnt[v - 1] += k
                k = 0

        # Compute final sum of squared differences
        return sum(v * v * cnt[v] for v in range(len(cnt)))