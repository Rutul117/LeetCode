from collections import defaultdict, deque

class Solution:
    def makeGraph(self, n, g):
        adj = defaultdict(list)

        for u, v in g:
            adj[u].append(v)

        return adj

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        sus = [0] * n
        sus[k] = 1

        # 1. Make graph
        adj = self.makeGraph(n, invocations)

        # 2. Mark all methods reachable from k as suspicious
        q = deque([k])

        while q:
            u = q.popleft()

            for v in adj[u]:
                if sus[v] == 0:
                    sus[v] = 1
                    q.append(v)

        # 3. Check if any non-suspicious method points to a suspicious method
        for u, v in invocations:
            if sus[u] == 0 and sus[v] == 1:
                # Cannot remove the suspicious group,
                # so literally nothing can be removed.
                return list(range(n))

        # Otherwise remove all suspicious methods
        return [i for i in range(n) if sus[i] == 0]