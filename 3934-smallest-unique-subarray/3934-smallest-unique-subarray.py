class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [{}]
        link = [-1]
        ln = [0]
        cnt = [0]
        last = 0
        for x in nums:
            cur = len(ln)
            nxt.append({})
            ln.append(ln[last] + 1)
            link.append(0)
            cnt.append(1)
            p = last
            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]
            if p != -1:
                q = nxt[p][x]
                if ln[p] + 1 == ln[q]:
                    link[cur] = q
                else:
                    cl = len(ln)
                    nxt.append(nxt[q].copy())
                    ln.append(ln[p] + 1)
                    link.append(link[q])
                    cnt.append(0)
                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = cl
                        p = link[p]
                    link[q] = link[cur] = cl
            last = cur
        m = len(ln)
        buckets = [0] * (n + 2)
        for v in range(m):
            buckets[ln[v]] += 1
        for i in range(1, n + 1):
            buckets[i] += buckets[i - 1]
        order = [0] * m
        for v in range(m - 1, -1, -1):
            buckets[ln[v]] -= 1
            order[buckets[ln[v]]] = v
        for i in range(m - 1, 0, -1):
            v = order[i]
            cnt[link[v]] += cnt[v]
        best = n
        for v in range(1, m):
            if cnt[v] == 1:
                t = ln[link[v]] + 1
                if t < best:
                    best = t
        return best