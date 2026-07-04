class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        from collections import deque
        q = deque([1])
        visited = set([1])
        ans = float('inf')
        
        while q:
            node = q.popleft()
            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return ans
