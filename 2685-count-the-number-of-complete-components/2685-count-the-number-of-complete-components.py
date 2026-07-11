class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            nodes = []
            while stack:
                u = stack.pop()
                if visited[u]:
                    continue
                visited[u] = True
                nodes.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        stack.append(v)
            return nodes

        complete_count = 0
        
        for i in range(n):
            if not visited[i]:
                comp_nodes = dfs(i)
                k = len(comp_nodes)

                # Count edges inside component
                edge_count = 0
                for u in comp_nodes:
                    edge_count += len(graph[u])
                
                edge_count //= 2  # because undirected count double
                
                # Check if complete: k*(k-1)/2 edges needed
                if edge_count == (k * (k - 1)) // 2:
                    complete_count += 1

        return complete_count
