class Solution:
    MOD = 10**9 + 7

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        ind = []
        for i, ch in enumerate(s):
            if ch != '0':
                ind.append((i, int(ch)))

        m = len(ind)

        last = [-1] * n
        j = -1
        for i in range(n):
            if s[i] != '0':
                j += 1
            last[i] = j

        nxt = [-1] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                j -= 1
            nxt[i] = j + 1
            if nxt[i] >= m:
                nxt[i] = -1

        prefSum = [0] * m
        curSum = 0
        for i in range(m):
            curSum += ind[i][1]
            prefSum[i] = curSum

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % self.MOD

        prefNum = [0] * m
        cur = 0
        for i in range(m):
            cur = (cur * 10 + ind[i][1]) % self.MOD
            prefNum[i] = cur

        ans = []

        for q in queries:
            l = nxt[q[0]]
            r = last[q[1]]

            if l == -1 or r == -1 or l > r:
                ans.append(0)
                continue

            digitSum = prefSum[r] - (prefSum[l - 1] if l > 0 else 0)

            num = prefNum[r]
            if l > 0:
                num = (num - prefNum[l - 1] * pow10[r - l + 1]) % self.MOD

            ans.append((num * digitSum) % self.MOD)

        return ans