class Solution:
    #@lru_cache
    def minMoves(self, classroom: List[str], energy: int) -> int:
        totL = 0
        litter_pos = {}
        st = None
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(classroom)
        cols = len(classroom[0])

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    st = (r, c)
                if classroom[r][c] == 'L':
                    litter_pos[(r, c)] = totL
                    totL += 1
        if totL == 0:
            return 0
        totLMask = (1<<totL) - 1
        @lru_cache
        def bfs():
            visit = {}
            q = deque([(st[0], st[1], energy, 0, 0)])
            moves = 0
            visit[(st[0], st[1], 0)] = energy
            while q:
                r, c, p, mask, moves = q.popleft()
                for i in range(4):
                    x, y = r+dirs[i][0], c+dirs[i][1]
                    if x < 0 or y < 0 or x == rows or y == cols or classroom[x][y] == 'X':
                        continue
                    new_p = p - 1
                    if classroom[x][y] == 'R':
                        new_p = energy
                    new_mask = mask
                    if classroom[x][y] == 'L':
                        new_mask |= (1 << litter_pos[(x, y)])
                    if new_mask == totLMask:
                        return moves+1
                    state = (x, y, new_mask)
                    if state in visit and visit[state] >= new_p:
                        continue
                    visit[state] = new_p
                    if new_p == 0:
                        continue
                    q.append((x, y, new_p, new_mask, moves+1))                        
            return -1
        return bfs()