from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        # 1. Information Kernels (The Adjacency Tensor)
        # Pre-calculating the kernels maximizes mutual information during the jump
        L = len(beginWord)
        adj = defaultdict(list)
        for word in word_set | {beginWord}:
            for i in range(L):
                kernel = word[:i] + "*" + word[i+1:]
                adj[kernel].append(word)
        
        # 2. Forward Propagation: Mapping the Distance Field
        # We store the shortest distance to each word to 'redact' non-optimal paths
        distances = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            # Level-by-level processing to maintain the 'Geodesic' constraint
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    found = True
                    break
                
                for i in range(L):
                    kernel = curr[:i] + "*" + curr[i+1:]
                    for neighbor in adj[kernel]:
                        if neighbor not in distances:
                            distances[neighbor] = distances[curr] + 1
                            queue.append(neighbor)
        
        if not found:
            return []
            
        # 3. Backward Reconstruction (The Gradient Bypass)
        # We trace from end to start to avoid exploring dead-ends in the manifold
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            d = distances[word]
            for i in range(L):
                kernel = word[:i] + "*" + word[i+1:]
                for neighbor in adj[kernel]:
                    # The Gradient Check: Only move toward the source
                    if distances.get(neighbor) == d - 1:
                        backtrack(neighbor, path + [neighbor])
        
        backtrack(endWord, [endWord])
        return res        