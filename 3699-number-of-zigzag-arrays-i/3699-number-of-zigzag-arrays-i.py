from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        value_count = r - l + 1

        ways = [0] + [1] * value_count

        for length in range(2, n + 1):
            prefix_sum = list(accumulate(ways))

            if length % 2 == 0:
                ways = [0] + prefix_sum[:-1]
            else:
                total_ways = prefix_sum[-1]
                ways = [0] + [(total_ways - prefix) % MOD for prefix in prefix_sum[1:]]

        return (sum(ways) % MOD * 2) % MOD